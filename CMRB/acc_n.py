import numpy as np
from relation_return import relation_map,two_ship,three_ship,solve_r2_return,solve_r3_return
def cal_acc(relationship_two_30,relationship_three_30,L0,L1,o,p):
    s=0
    for ii in range (0,15000):
        d=np.load('D:\\zsk\\RAVEN\\data_9_test\\'+str(ii)+'.npy')
        c=np.load('D:\\zsk\\RAVEN\\select8_test\\'+str(ii)+'.npy')
        relationship_two,relationship_three=relation_map(d)
        for i in range (0,30):
            L1_2=0
            L1_3=0
            eq2_0=np.where(relationship_two_30[0:8,0:8,i]==relationship_two[0:8,0:8])[0]
            eq2_1=np.where(relationship_two_30[0:8,0:8,i]==relationship_two[0:8,0:8])[1]
            eq3_0=np.where(relationship_three_30[0:8,0:8,0:8,i]==relationship_three[0:8,0:8,0:8])[0]
            eq3_1=np.where(relationship_three_30[0:8,0:8,0:8,i]==relationship_three[0:8,0:8,0:8])[1]
            eq3_2=np.where(relationship_three_30[0:8,0:8,0:8,i]==relationship_three[0:8,0:8,0:8])[2]
            for a in range (0,eq2_0.size):
                if relationship_two_30[:,:,i][eq2_0[a]][eq2_1[a]]!=0:
                    if relationship_two[eq2_0[a]][eq2_1[a]]!=0:
                        L1_2+=1
            for b in range (0,eq3_0.size):
                if relationship_three_30[:,:,:,i][eq3_0[b]][eq3_1[b]][eq3_2[b]]!=0:
                    if relationship_three[eq3_0[b]][eq3_1[b]][eq3_2[b]]!=0:
                        L1_3+=1
            if i not in o:
                if L1_2>=L0:
                    relationship_two_copy=relationship_two.copy()
                    relationship_two_copy[relationship_two_copy!=relationship_two_30[:,:,i]]=0
                    pr2=solve_r2_return(relationship_two_copy,d)
                    if pr2==d[8]:
                        s1=1
                    else:
                        s1=0
                    s+=s1
                        #count[i]+=1
                        #relationship_two_30[:,:,i]=relationship_two
                    if pr2 in c:
                        break
            if i not in p:
                if L1_3>=L1:
                    relationship_three_copy=relationship_three.copy()
                    relationship_three_copy[relationship_three_copy!=relationship_three_30[:,:,:,i]]=0
                    pr3=solve_r3_return(relationship_three_copy,d)
                    if pr3==d[8]:
                        s2=1
                    else:
                        s2=0
                    s+=s2
                        #count[i]+=1
                        #relationship_three_30[:,:,:,i]=relationship_three
                    if pr3 in c:
                        break
                

    print(s/15000)
    return s/15000