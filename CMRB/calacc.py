import numpy as np
from acc_n_1 import cal_acc
L0=7
L1=2
relationship_two_30=np.load('CM3\\ts2'+'_'+str(L0)+'_'+str(L1)+'.npy')
relationship_three_30=np.load('CM3\\ts3'+'_'+str(L0)+'_'+str(L1)+'.npy')
acc=cal_acc(relationship_two_30,relationship_three_30,L0,L1,[],[])
print(acc)
