import numpy as np
def types_template(types):
    predict=np.ones(4)*(-1)
    template=np.ones(4)*(-1)
    for i in range (0,4):
        if (types[i,:]!=-1).any():
            predict[i],template[i]=general_template(types[i,:])
    return predict,template