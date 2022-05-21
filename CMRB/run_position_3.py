import numpy as np
from relation_position_3 import relation_map,two_ship,three_ship,solve_r2,solve_r3
from acc_p1_3 import cal_acc
from acc_p2_3 import cal_al
acc_all=np.zeros((4,3))
for L0 in range (4,8):
    for L1 in range (1,4):
        relationship_two_30=np.zeros((9,9,30))
        relationship_three_30=np.zeros((9,9,9,30))
        count=np.zeros(30)
        count1=np.zeros(30)
        tr=np.zeros(30)
        tr1=np.zeros(30)
        d_old=np.zeros((3,3,9,30))
        d_old1=np.zeros((3,3,9,30))
        for ii in range (0,10000):
            s=0
            s1=1
            d=np.load('D:\\zsk\\RAVEN\\position9_3\\'+str(ii)+'.npy')
            relationship_two,relationship_three=relation_map(d)
            for i in range (0,30):
                L1_2=0
                eq2_0=np.where(relationship_two_30[0:8,0:8,i]==relationship_two[0:8,0:8])[0]
                eq2_1=np.where(relationship_two_30[0:8,0:8,i]==relationship_two[0:8,0:8])[1]
                for a in range (0,eq2_0.size):
                    if relationship_two_30[:,:,i][eq2_0[a]][eq2_1[a]]!=0:
                        if relationship_two[eq2_0[a]][eq2_1[a]]!=0:
                            L1_2+=1
                if L1_2>=L0:
                    if relationship_two_30[:,:,i][relationship_two_30[:,:,i]>0].size>9:
                        relationship_two_copy=relationship_two.copy()
                        relationship_two_copy[relationship_two_copy!=relationship_two_30[:,:,i]]=0
                        if relationship_two_copy[relationship_two_copy>0].size>=9:
                            s=solve_r2(relationship_two_copy,d)
                            if s==1:
                                count[i]+=1
                                tr[i]=ii
                                if (d_old[:,:,:,i]!=0).any():
                                    s1=solve_r2(relationship_two_copy,d_old[:,:,:,i])
                                if s1==1:
                                    relationship_two_30[:,:,i]=relationship_two_copy
                                break
                    if relationship_two_30[:,:,i][relationship_two_30[:,:,i]>0].size==9:
                        s=solve_r2(relationship_two_30[:,:,i],d)
                        if s==1:
                            count[i]+=1
                            tr[i]=ii
                            break
            if s==0:
                for i in range (0,30):
                    L1_3=0
                    eq3_0=np.where(relationship_three_30[0:8,0:8,0:8,i]==relationship_three[0:8,0:8,0:8])[0]
                    eq3_1=np.where(relationship_three_30[0:8,0:8,0:8,i]==relationship_three[0:8,0:8,0:8])[1]
                    eq3_2=np.where(relationship_three_30[0:8,0:8,0:8,i]==relationship_three[0:8,0:8,0:8])[2]
                    for b in range (0,eq3_0.size):
                        if relationship_three_30[:,:,:,i][eq3_0[b]][eq3_1[b]][eq3_2[b]]!=0:
                            if relationship_three[eq3_0[b]][eq3_1[b]][eq3_2[b]]!=0:
                                L1_3+=1
                    if L1_3>=L1:
                        if relationship_three_30[:,:,:,i][relationship_three_30[:,:,:,i]>0].size>3:
                            relationship_three_copy=relationship_three.copy()
                            relationship_three_copy[relationship_three_copy!=relationship_three_30[:,:,:,i]]=0
                            if relationship_three_copy[relationship_three_copy>0].size>=3:
                                s=solve_r3(relationship_three_copy,d)
                                if s==1:
                                    count1[i]+=1
                                    tr1[i]=ii
                                    if (d_old1[:,:,:,i]!=0).any():
                                        s1=solve_r3(relationship_three_copy,d_old1[:,:,:,i])
                                    if s1==1:
                                        relationship_three_30[:,:,:,i]=relationship_three_copy
                                    break
                        if relationship_three_30[:,:,:,i][relationship_three_30[:,:,:,i]>0].size==3:
                            s=solve_r3(relationship_three_30[:,:,:,i],d)
                            if s==1:
                                count1[i]+=1
                                tr1[i]=ii
                                break

            if s==0:
                relationship_two_30[:,:,np.argmin(count)]=relationship_two
                relationship_three_30[:,:,:,np.argmin(count1)]=relationship_three
                d_old[:,:,:,np.argmin(count)]=d
                d_old1[:,:,:,np.argmin(count1)]=d
                tr[np.argmin(count)]=ii
                tr1[np.argmin(count1)]=ii
                count[np.argmin(count)]=0
                count1[np.argmin(count1)]=0
            relationship_two_30[:,:,np.where((ii-tr)>1500)[0]]=0
            relationship_three_30[:,:,:,np.where((ii-tr1)>1500)[0]]=0
            d_old[:,:,:,np.where((ii-tr)>1500)[0]]=0
            d_old1[:,:,:,np.where((ii-tr1)>1500)[0]]=0
            count[np.where((ii-tr)>1500)[0]]=0
            count1[np.where((ii-tr1)>1500)[0]]=0
            if ii%1000==1:
                print(count)
                print('count1')
                print(count1)
                np.save('CMP3_2\\ts2'+str(ii)+'_'+str(L0)+'_'+str(L1)+'.npy',relationship_two_30)
                np.save('CMP3_2\\ts3'+str(ii)+'_'+str(L0)+'_'+str(L1)+'.npy',relationship_three_30)
            if ii==9999:
                relationship_two_30[:,:,np.where(count<2)[0]]=0
                relationship_three_30[:,:,:,np.where(count1<2)[0]]=0
        np.save('CMP3_2\\ts2'+'_'+str(L0)+'_'+str(L1)+'.npy',relationship_two_30)
        np.save('CMP3_2\\ts3'+'_'+str(L0)+'_'+str(L1)+'.npy',relationship_three_30)
        o,p=cal_al(relationship_two_30,relationship_three_30,L0,L1)
        print(o)
        print(p)
        np.save('CMP3_2\\o'+str(L0)+'_'+str(L1)+'.npy',o)
        np.save('CMP3_2\\p'+str(L0)+'_'+str(L1)+'.npy',p)
        acc_all[L0-4,L1-1]=cal_acc(relationship_two_30,relationship_three_30,L0,L1,o,p)
        print(acc_all[L0-4,L1-1])
print(acc_all)
np.save('CMP3_2\\acc.npy',acc_all)
