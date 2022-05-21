import numpy as np
def progression_place_template_twobytwo(Exist):
    predict1=np.zeros((2,2))
    if Exist[0,0]==1:
        predict1[0,1]=1
    if Exist[0,1]==1:
        predict1[1,0]=1
    if Exist[1,0]==1:
        predict1[1,1]=1
    if Exist[1,1]==1:
        predict1[0,0]=1
    return predict1

def progression_place_template1_twobytwo(Exist):
    predict1=np.zeros((2,2))
    if Exist[0,0]==1:
        predict1[1,1]=1
    if Exist[0,1]==1:
        predict1[0,0]=1
    if Exist[1,0]==1:
        predict1[0,1]=1
    if Exist[1,1]==1:
        predict1[1,0]=1
    return predict1

def progression_place_template_threebythree(Exist):
    predict1=np.zeros((3,3))
    for i in range (0,3):
        for j in range (0,3):
            if Exist[i,j]==1 and j<2:
                predict1[i,j+1]=1
            if Exist[i,j]==1 and j==2 and i<2:
                predict1[i+1,0]=1
            if Exist[i,j]==1 and j==2 and i==2:
                predict1[0,0]=1
    return predict1

def progression_place_template1_threebythree(Exist):
    predict1=np.zeros((3,3))
    for i in range (0,3):
        for j in range (0,3):
            if Exist[i,j]==1 and j>0:
                predict1[i,j-1]=1
            if Exist[i,j]==1 and j==0 and i>0:
                predict1[i-1,2]=1
            if Exist[i,j]==1 and j==0 and i==0:
                predict1[2,2]=1
    return predict1

def multiple_progression_place_number(Exist0,Exist1):
    predict1=np.zeros((3,3))
    n=-1
    if Exist1!=[]:
        for i in range (0,9):
            if i==0:
                predict1=progression_place_template_threebythree(Exist0)
            if i>0:
                predict1=progression_place_template_threebythree(predict1)
            if (predict1==Exist1).all():
                n=i
    return n
def multiple_progression_place_template(Exist0,n):
    predict1=np.ones((3,3))*-1
    for i in range (0,n+1):
        if i==0:
            predict1=progression_place_template_threebythree(Exist0)
        if i>0:
            predict1=progression_place_template_threebythree(predict1)
    return predict1

def minus_place_template1(Exist):
    predict1=Exist[:,:,0]-Exist[:,:,1]
    predict1[predict1<0]=0
    return predict1

def minus_place_template2(Exist):
    predict1=Exist[:,:,1]-Exist[:,:,0]
    predict1[predict1<0]=0
    return predict1

def plus_place_template(Exist):
    predict1=Exist[:,:,1]+Exist[:,:,0]
    predict1[predict1>1]=1
    return predict1


def place_template(Exist,problem_set):
    template=-1
    if problem_set==1 or problem_set==4:
        predict=np.ones((2,2))*(-1)
        
    if problem_set==2:
        predict=np.ones((3,3))*(-1)
    #template 1
    
    #print(progression_place_template(Exist[:,:,0]))
    #print(Exist[:,:,1])
    if problem_set==1 or problem_set==4:
        if (progression_place_template_twobytwo(Exist[:,:,0])==Exist[:,:,1]).all() and (progression_place_template_twobytwo(Exist[:,:,1])==Exist[:,:,2]).all():
            if (progression_place_template_twobytwo(Exist[:,:,3])==Exist[:,:,4]).all() and (progression_place_template_twobytwo(Exist[:,:,4])==Exist[:,:,5]).all():
                if (progression_place_template_twobytwo(Exist[:,:,6])==Exist[:,:,7]).all():
                    predict=progression_place_template_twobytwo(Exist[:,:,7])
                    template=1

        if (progression_place_template1_twobytwo(Exist[:,:,0])==Exist[:,:,1]).all() and (progression_place_template1_twobytwo(Exist[:,:,1])==Exist[:,:,2]).all():
            if (progression_place_template1_twobytwo(Exist[:,:,3])==Exist[:,:,4]).all() and (progression_place_template1_twobytwo(Exist[:,:,4])==Exist[:,:,5]).all():
                if (progression_place_template1_twobytwo(Exist[:,:,6])==Exist[:,:,7]).all():
                    #print('1')
                    predict=progression_place_template1_twobytwo(Exist[:,:,7])
                    template=1
    if problem_set==2:
        if (progression_place_template_threebythree(Exist[:,:,0])==Exist[:,:,1]).all() and (progression_place_template_threebythree(Exist[:,:,1])==Exist[:,:,2]).all():
            if (progression_place_template_threebythree(Exist[:,:,3])==Exist[:,:,4]).all() and (progression_place_template_threebythree(Exist[:,:,4])==Exist[:,:,5]).all():
                if (progression_place_template_threebythree(Exist[:,:,6])==Exist[:,:,7]).all():
                    predict=progression_place_template_threebythree(Exist[:,:,7])
                    template=1

        if (progression_place_template1_threebythree(Exist[:,:,0])==Exist[:,:,1]).all() and (progression_place_template1_threebythree(Exist[:,:,1])==Exist[:,:,2]).all():
            if (progression_place_template1_threebythree(Exist[:,:,3])==Exist[:,:,4]).all() and (progression_place_template1_threebythree(Exist[:,:,4])==Exist[:,:,5]).all():
                if (progression_place_template1_threebythree(Exist[:,:,6])==Exist[:,:,7]).all():
                    #print('1')
                    predict=progression_place_template1_threebythree(Exist[:,:,7])
                    template=1
        n1=multiple_progression_place_number(Exist[:,:,0],Exist[:,:,1])
        n2=multiple_progression_place_number(Exist[:,:,1],Exist[:,:,2])
        if n1!=-1 and n2!=-1:
            if (multiple_progression_place_template(Exist[:,:,3],n1)==Exist[:,:,4]).all() and (multiple_progression_place_template(Exist[:,:,4],n2)==Exist[:,:,5]).all():
                if (multiple_progression_place_template(Exist[:,:,6],n1)==Exist[:,:,7]).all():
                    predict=multiple_progression_place_template(Exist[:,:,7],n2)
                    template=1
    #template 2
    if (minus_place_template1(Exist[:,:,0:2])==Exist[:,:,2]).all() and (minus_place_template1(Exist[:,:,3:5])==Exist[:,:,5]).all():
        predict=minus_place_template1(Exist[:,:,6:8])
        template=2
        
    if (minus_place_template2(Exist[:,:,0:2])==Exist[:,:,2]).all() and (minus_place_template2(Exist[:,:,3:5])==Exist[:,:,5]).all():
        predict=minus_place_template2(Exist[:,:,6:8])
        template=2
        
    if (plus_place_template(Exist[:,:,0:2])==Exist[:,:,2]).all() and (plus_place_template(Exist[:,:,3:5])==Exist[:,:,5]).all():
        predict=plus_place_template(Exist[:,:,6:8])
        template=2
    #template 3
    #print((Exist[:,:,1]==Exist[:,:,5]==Exist[:,:,6]).all())
    if (Exist[:,:,0]==Exist[:,:,4]).all() and (Exist[:,:,1]==Exist[:,:,5]).all() and (Exist[:,:,5]==Exist[:,:,6]).all() and (Exist[:,:,2]==Exist[:,:,3]).all() and (Exist[:,:,3]==Exist[:,:,7]).all():
        predict=Exist[:,:,0]
        template=3
    if (Exist[:,:,1]==Exist[:,:,3]).all() and (Exist[:,:,2]==Exist[:,:,4]).all() and (Exist[:,:,4]==Exist[:,:,6]).all() and (Exist[:,:,0]==Exist[:,:,5]).all() and (Exist[:,:,5]==Exist[:,:,7]).all():
        predict=Exist[:,:,1]
        template=3
        
    if (Exist[:,:,0]==Exist[:,:,1]).all() and (Exist[:,:,1]==Exist[:,:,2]).all():
        if (Exist[:,:,3]==Exist[:,:,4]).all() and (Exist[:,:,4]==Exist[:,:,5]).all():
            if (Exist[:,:,6]==Exist[:,:,7]).all():
                predict=Exist[:,:,7]
                template=4
    return predict,template



def place_types_template(types,problem_set):
    #types shape 4,8,2,2
    s=types.shape[0]
    s1=types.shape[3]
    predict=np.ones((s,s1,s1))*(-1)
    template=np.ones((s))*(-1)
    identical=np.zeros((s,s,2))
    valid=s
    for i in range (0,s):
        if (types[i,:,:,:]==np.ones((8,s1,s1))*(-1)).all():
            valid-=1

    #constant
    # for i in range (0,4):
    #     for j in range (0,4):
    #         if (types[i,:,:,:]!=-1).any() and (types[j,:,:,:]!=-1).any():
    #             if (types[j,3:6,:,:]==types[i,0:3,:,:]).all():
    #                 identical[i,j,0]=1
    #             if (types[j,6:8,:,:]==types[i,0:2,:,:]).all():
    #                 identical[i,j,1]=1
    # if np.sum(identical[:,:,0])==valid:
    #     if np.sum(identical[:,:,1])==valid:
    # # for w in range (0,np.where(identical[:,:,1]==1)[0].size):
    # #     predict[np.where(identical[:,:,1]==1)[1][w],:,:]=types[np.where(identical[:,:,1]==1)[0][w],2,:,:]
    #         for w in range (0,np.where(identical[:,:,1]==1)[0].size):
    #             predict[np.where(identical[:,:,1]==1)[1][w],:,:]=types[np.where(identical[:,:,1]==1)[0][w],2,:,:]
    #             template[np.where(identical[:,:,1]==1)[1][w]]=1

    #progression
    if problem_set==1 or problem_set==4:
        for i in range (0,4):
            if (progression_place_template_twobytwo(types[i,0,:,:])==types[i,1,:,:]).all() and (progression_place_template_twobytwo(types[i,1,:,:])==types[i,2,:,:]).all():
                if (progression_place_template_twobytwo(types[i,3,:,:])==types[i,4,:,:]).all() and (progression_place_template_twobytwo(types[i,4,:,:])==types[i,5,:,:]).all():
                    if (progression_place_template_twobytwo(types[i,6,:,:])==types[i,7,:,:]).all():
                        predict[i,:,:]=progression_place_template_twobytwo(Exist[:,:,7])
                        template[i]=1
        for i in range (0,4):
            if (progression_place_template1_twobytwo(types[i,0,:,:])==types[i,1,:,:]).all() and (progression_place_template1_twobytwo(types[i,1,:,:])==types[i,2,:,:]).all():
                if (progression_place_template1_twobytwo(types[i,3,:,:])==types[i,4,:,:]).all() and (progression_place_template1_twobytwo(types[i,4,:,:])==types[i,5,:,:]).all():
                    if (progression_place_template1_twobytwo(types[i,6,:,:])==types[i,7,:,:]).all():
                        predict[i,:,:]=progression_place_template1_twobytwo(Exist[:,:,7])
                        template[i]=1
    if problem_set==2:
        for i in range (0,s):
            if (progression_place_template_threebythree(types[i,0,:,:])==types[i,1,:,:]).all() and (progression_place_template_threebythree(types[i,1,:,:])==types[i,2,:,:]).all():
                if (progression_place_template_threebythree(types[i,3,:,:])==types[i,4,:,:]).all() and (progression_place_template_threebythree(types[i,4,:,:])==types[i,5,:,:]).all():
                    if (progression_place_template_threebythree(types[i,6,:,:])==types[i,7,:,:]).all():
                        predict[i,:,:]=progression_place_template_threebythree(Exist[:,:,7])
                        template[i]=1
        for i in range (0,s):
            if (progression_place_template1_threebythree(types[i,0,:,:])==types[i,1,:,:]).all() and (progression_place_template1_threebythree(types[i,1,:,:])==types[i,2,:,:]).all():
                if (progression_place_template1_threebythree(types[i,3,:,:])==types[i,4,:,:]).all() and (progression_place_template1_threebythree(types[i,4,:,:])==types[i,5,:,:]).all():
                    if (progression_place_template1_threebythree(types[i,6,:,:])==types[i,7,:,:]).all():
                        predict[i,:,:]=progression_place_template1_threebythree(Exist[:,:,7])
                        template[i]=1
        for i in range (0,s):
            n1=multiple_progression_place_number(types[i,0,:,:],types[i,1,:,:])
            n2=multiple_progression_place_number(types[i,1,:,:],types[i,2,:,:])
            if n1!=-1 and n2!=-1:
                if (multiple_progression_place_template(types[i,3,:,:],n1)==types[i,4,:,:]).all() and (multiple_progression_place_template(types[i,4,:,:],n2)==types[i,5,:,:]).all():
                    if (multiple_progression_place_template(types[i,6,:,:],n1)==types[i,7,:,:]).all():
                        predict[i,:,:]=multiple_progression_place_template(types[i,7,:,:],n2)
                        template[i]=1
            
        
    #distribute three or constant
    identical=np.zeros((s,s,2))
    for i in range (0,s):
        ttypes=np.zeros((3,s1,s1))
        ttypes[0,:,:]=types[i,1,:,:]
        ttypes[1,:,:]=types[i,2,:,:]
        ttypes[2,:,:]=types[i,0,:,:]

        ttypes1=np.zeros((3,s1,s1))
        ttypes1[0,:,:]=types[i,2,:,:]
        ttypes1[1,:,:]=types[i,0,:,:]
        ttypes1[2,:,:]=types[i,1,:,:]

        ttypes2=np.zeros((3,s1,s1))
        ttypes2[0,:,:]=types[i,1,:,:]
        ttypes2[1,:,:]=types[i,0,:,:]
        ttypes2[2,:,:]=types[i,2,:,:]

        ttypes3=np.zeros((3,s1,s1))
        ttypes3[0,:,:]=types[i,2,:,:]
        ttypes3[1,:,:]=types[i,1,:,:]
        ttypes3[2,:,:]=types[i,0,:,:]

        ttypes4=np.zeros((3,s1,s1))
        ttypes4[0,:,:]=types[i,0,:,:]
        ttypes4[1,:,:]=types[i,2,:,:]
        ttypes4[2,:,:]=types[i,1,:,:]
        for j in range (0,s):
            if (types[i,:,:,:]!=-1).any() and (types[j,:,:,:]!=-1).any():
                if (types[j,3:6,:,:]==types[i,0:3,:,:]).all() or (types[j,3:6,:,:]==ttypes).all() or (types[j,3:6,:,:]==ttypes1).all() or (types[j,3:6,:,:]==ttypes2).all() or (types[j,3:6,:,:]==ttypes3).all() or (types[j,3:6,:,:]==ttypes4).all():
                    #print('1')
                    if np.sum(identical[i,:,0])==0 and np.sum(identical[:,j,0])==0:
                        #print('2')
                        identical[i,j,0]=1
                if (types[j,6:8,:,:]==types[i,0:2,:,:]).all() or (types[j,6:8,:,:]==ttypes[0:2,:,:]).all() or (types[j,6:8,:,:]==ttypes1[0:2,:,:]).all() or (types[j,6:8,:,:]==ttypes2[0:2,:,:]).all() or (types[j,6:8,:,:]==ttypes3[0:2,:,:]).all() or (types[j,6:8,:,:]==ttypes4[0:2,:,:]).all():
                    #print('1')
                    if np.sum(identical[i,:,1])==0 and np.sum(identical[:,j,1])==0:
                        identical[i,j,1]=1
                        #print('2')
    #print(valid)
    #print(np.sum(identical[:,:,0]))
    if np.sum(identical[:,:,0])==valid:
        if np.sum(identical[:,:,1])==valid:
            for w in range (0,np.where(identical[:,:,1]==1)[0].size):
                p=np.zeros(3)
                for i in range (6,8):
                    for j in range (0,3):
                        if (types[np.where(identical[:,:,1]==1)[1][w],i,:,:]==types[np.where(identical[:,:,1]==1)[0][w],j,:,:]).all():
                            if np.sum(p)<=1:
                                p[j]=1
                predict[np.where(identical[:,:,1]==1)[1][w],:,:]=types[np.where(identical[:,:,1]==1)[0][w],np.where(p==0)[0][0],:,:]
                template[np.where(identical[:,:,1]==1)[1][w]]=2
    return predict,template