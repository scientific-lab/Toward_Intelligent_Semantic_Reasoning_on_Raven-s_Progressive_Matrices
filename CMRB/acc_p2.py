import numpy as np
from relation_position import relation_map,two_ship,three_ship,solve_r2_return,solve_r3_return
def cal_al(relationship_two_30,relationship_three_30,L0,L1):
    s=0
    l=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    l1=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    ll1=[]
    ll2=[]
    
    for ii in range (0,10000):
        d=np.load('D:\\zsk\\RAVEN\\position9\\'+str(ii)+'.npy')
        c=np.load('D:\\zsk\\RAVEN\\pselection9\\'+str(ii)+'.npy')
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
            if L1_2>=5:
                pr2=solve_r2_return(relationship_two_30[:,:,i],d)
                if (pr2==d[:,:,8]).all():
                  s1=1
                  l[i].append(ii)
                else:
                  s1=0
                s+=s1
                    #count[i]+=1
                    #relationship_two_30[:,:,i]=relationship_two
            if L1_3>=2:
                pr3=solve_r3_return(relationship_three_30[:,:,:,i],d)
                if (pr3==d[:,:,8]).all():
                  s2=1
                  l1[i].append(ii)
                else:
                  s2=0
                s+=s2
                    #count[i]+=1
                    #relationship_three_30[:,:,:,i]=relationship_three

                

    for a in range (0,30):
        for b in range (0,30):
            if set(l[a])< set(l[b]):
                if a not in ll1:
                    ll1.append(a)
            if set(l[a])<set(l1[b]):
                if a not in ll1:
                    ll1.append(a)
            if set(l1[a])<set(l1[b]):
                if a not in ll2:
                    ll2.append(a)
            if set(l1[a])<set(l[b]):
                if a not in ll2:
                    ll2.append(a)
    np.save('l_position_no3'+str(L0)+'_'+str(L1)+'.npy',l)
    np.save('l1_position_no3'+str(L0)+'_'+str(L1)+'.npy',l1)
           
    return ll1,ll2