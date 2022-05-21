import numpy as np
from relation_return import relation_map_in,two_ship,three_ship,solve_r2_return,solve_r3_return
def CM(relationship_two_30,relationship_three_30,o,p,d,c):
    pr2=-1
    tem=-1
    relationship_two,relationship_three=relation_map_in(d)
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
            if L1_2>=7:
                pr2=solve_r2_return(relationship_two_30[:,:,i],d)
                if pr2 in c:
                    tem=i
                    break
        if i not in p:
            if L1_3>=2:
                pr2=solve_r3_return(relationship_three_30[:,:,:,i],d)
                if pr2 in c:
                    tem=30+i
                    break



    return pr2,tem