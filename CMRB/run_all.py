from solve_all import solve_and_draw
import os
import numpy as np
Name_of_dir=['center_single','distribute_four','distribute_nine','in_center_single_out_center_single','in_distribute_four_out_center_single','left_center_single_right_center_single','up_center_single_down_center_single']
# direct_to_dir=['/nfs/h1/RAVEN/I-RAVEN/','/nfs/h1/RAVEN/RAVEN-FAIR/']
#direct_to_dir=['/nfs/h1/RAVEN/RAVEN-FAIR/']
direct_to_dir=['D:\\zsk\\RAVEN\\RAVEN_ori\\','D:\\zsk\\RAVEN\\I-RAVEN\\','D:\\zsk\\RAVEN\\RAVEN-FAIR\\']
#savestr='raven-fair-new'
for dirs in direct_to_dir:
    if dirs=='/nfs/h1/RAVEN/RAVEN_ori/':
        savestr='ori'
    if dirs=='/nfs/h1/RAVEN/I-RAVEN/':
        savestr='iraven'
    if dirs=='/nfs/h1/RAVEN/RAVEN-FAIR/':
        savestr='fair'
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
                    Answer[name_ind]=solve_and_draw(data,0)
                    correct[name_ind]=np.load(dirs+Name_id+'\\'+n)['target']
        incorrect_size=np.where(Answer!=correct)[0].size
        print(dirs+Name_id+' accuracy: '+str(1-incorrect_size/10000))
        np.save(savestr+Name_id+'acc.npy',1-incorrect_size/10000)