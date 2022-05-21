import numpy as np
def general_template(Attribute):
    template=-2
    predict=-2
    #template 2
    if Attribute[0]+Attribute[1]==Attribute[2] and Attribute[3]+Attribute[4]==Attribute[5]:
        predict=Attribute[6]+Attribute[7]
        template=2
    if Attribute[0]-Attribute[1]==Attribute[2] and Attribute[3]-Attribute[4]==Attribute[5]:
        predict=Attribute[6]-Attribute[7]
        template=2
    if Attribute[1]-Attribute[0]==Attribute[2] and Attribute[4]-Attribute[3]==Attribute[5]:
        predict=Attribute[7]-Attribute[6]
        template=2
        
    w1=Attribute[2]-(Attribute[0]+Attribute[1])
    if Attribute[5]-(Attribute[3]+Attribute[4])==w1 and w1>0:
        predict=Attribute[6]+Attribute[7]+w1
        template=2
        
    w2=Attribute[0]-Attribute[1]-Attribute[2]
    if Attribute[3]-Attribute[4]-Attribute[5]==w2 and w2>0:
        predict=Attribute[6]-Attribute[7]-w2
        template=2
        
    w3=Attribute[1]-Attribute[0]-Attribute[2]
    if Attribute[4]-Attribute[3]-Attribute[5]==w3 and w3>0:
        predict=Attribute[7]-Attribute[6]-w3
        template=2
        
    #template 1
    n1=Attribute[1]-Attribute[0]
    n2=Attribute[2]-Attribute[1]
    if Attribute[4]-Attribute[3]==n1 and Attribute[5]-Attribute[4]==n2:
        if Attribute[7]-Attribute[6]==n1:
            predict=Attribute[7]+n2
            template=1
    #template 3
    if Attribute[0]==Attribute[4] and Attribute[1]==Attribute[5]==Attribute[6] and Attribute[2]==Attribute[3]==Attribute[7]:
        predict=Attribute[4]
        template=3
    if Attribute[1]==Attribute[3] and Attribute[2]==Attribute[4]==Attribute[6] and Attribute[0]==Attribute[5]==Attribute[7]:
        predict=Attribute[3]
        template=3
    if (Attribute==-1).any():
        predict=-1
        template=-1
    return predict,template

def types_template(types):
    s=types.shape[0]
    predict=np.ones(s)*(-1)
    template=np.ones(s)*(-1)
    for i in range (0,s):
        if (types[i,:]!=-1).any():
            predict[i],template[i]=general_template(types[i,:])
    return predict,template