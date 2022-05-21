import numpy as np
from acc_p1_3 import cal_acc
L0=4
L1=2
relationship_two_30=np.load('CMP3\\ts2'+'_'+str(L0)+'_'+str(L1)+'.npy')
relationship_three_30=np.load('CMP3\\ts3'+'_'+str(L0)+'_'+str(L1)+'.npy')
o=np.load('CMP3\\o'+str(L0)+'_'+str(L1)+'.npy')
p=np.load('CMP3\\p'+str(L0)+'_'+str(L1)+'.npy')
acc=cal_acc(relationship_two_30,relationship_three_30,L0,L1,o,p)
print(acc)
