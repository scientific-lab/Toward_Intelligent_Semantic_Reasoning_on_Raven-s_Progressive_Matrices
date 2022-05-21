from solve_cm import solve_and_draw
import os
import numpy as np
Name_of_dir=['center_single','distribute_four','distribute_nine','in_center_single_out_center_single','in_distribute_four_out_center_single','left_center_single_right_center_single','up_center_single_down_center_single']
# direct_to_dir=['/nfs/h1/RAVEN/I-RAVEN/','/nfs/h1/RAVEN/RAVEN-FAIR/']
#direct_to_dir=['/nfs/h1/RAVEN/RAVEN_ori/']
direct_to_dir=['D:\\zsk\\RAVEN\\I-RAVEN\\']
savestr='raven_iraven_cm2'
r2_30=np.load('CM6\\ts2_final_4_2.npy')
r3_30=np.load('CM6\\ts3_final_4_2.npy')
o=np.load('CM6\\o_final4_2.npy')
p=np.load('CM6\\p_final4_2.npy')
r2p2_30=np.load('CMP_2\\ts2_3_1.npy')
r3p2_30=np.load('CMP_2\\ts3_3_1.npy')
op2=np.load('CMP_2\\o3_1.npy')
pp2=np.load('CMP_2\\p3_1.npy')
r2p3_30=np.load('CMP3_2\\ts2_4_2.npy')
r3p3_30=np.load('CMP3_2\\ts3_4_2.npy')
op3=np.load('CMP3_2\\o4_2.npy')
pp3=np.load('CMP3_2\\p4_2.npy')
for dirs in direct_to_dir:
#     if dirs=='/nfs/h1/RAVEN/I-RAVEN/':
#         savestr='iraven'
#     if dirs=='/nfs/h1/RAVEN/RAVEN-FAIR/':
#         savestr='fair'
    for Name_id in Name_of_dir:
        Name=os.listdir(dirs+Name_id)
        Answer=np.zeros(10000)
        correct=np.zeros(10000)
        for name_ind in range (0,10000):
        #for name_ind in [0,1]:
            length=len('RAVEN_'+str(name_ind)+'_')
            for n in Name:
                if n[0:length]=='RAVEN_'+str(name_ind)+'_' and n[-3:]=='npz':
                    data=np.load(dirs+Name_id+'\\'+n)['image']
                    Answer[name_ind]=solve_and_draw(data,0,r2_30,r3_30,o,p,r2p2_30,r3p2_30,op2,pp2,r2p3_30,r3p3_30,op3,pp3)
                    correct[name_ind]=np.load(dirs+Name_id+'\\'+n)['target']
        incorrect_size=np.where(Answer!=correct)[0].size
        print(dirs+Name_id+' accuracy: '+str(1-incorrect_size/10000))
        np.save(savestr+Name_id+'acc.npy',1-incorrect_size/10000)