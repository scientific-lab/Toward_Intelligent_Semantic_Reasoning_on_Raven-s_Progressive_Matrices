import numpy as np
def place_types_template(types):
    #types shape 4,8,2,2
    predict=np.ones((4,2,2))*(-1)
    template=np.ones((4))*(-1)
    identical=np.zeros((4,4,2))
    valid=0
    for i in range (0,4):
        if (types[i,:,:,:]==np.ones((8,2,2))*(-1)).all():
            valid=i

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
    for i in range (0,4):
        if (progression_place_template(types[i,0,:,:])==types[i,1,:,:]).all() and (progression_place_template(types[i,1,:,:])==types[i,2,:,:]).all():
            if (progression_place_template(types[i,3,:,:])==types[i,4,:,:]).all() and (progression_place_template(types[i,4,:,:])==types[i,5,:,:]).all():
                if (progression_place_template(types[i,6,:,:])==types[i,7,:,:]).all():
                    predict[i,:,:]=progression_place_template(Exist[:,:,7])
                    template[i]=1
    for i in range (0,4):
        if (progression_place_template1(types[i,0,:,:])==types[i,1,:,:]).all() and (progression_place_template1(types[i,1,:,:])==types[i,2,:,:]).all():
            if (progression_place_template1(types[i,3,:,:])==types[i,4,:,:]).all() and (progression_place_template1(types[i,4,:,:])==types[i,5,:,:]).all():
                if (progression_place_template1(types[i,6,:,:])==types[i,7,:,:]).all():
                    predict[i,:,:]=progression_place_template1(Exist[:,:,7])
                    template[i]=1
    #distribute three or constant
    identical=np.zeros((4,4,2))
    for i in range (0,4):
        ttypes=np.zeros((3,2,2))
        ttypes[0,:,:]=types[i,1,:,:]
        ttypes[1,:,:]=types[i,2,:,:]
        ttypes[2,:,:]=types[i,0,:,:]

        ttypes1=np.zeros((3,2,2))
        ttypes1[0,:,:]=types[i,2,:,:]
        ttypes1[1,:,:]=types[i,0,:,:]
        ttypes1[2,:,:]=types[i,1,:,:]

        ttypes2=np.zeros((3,2,2))
        ttypes2[0,:,:]=types[i,1,:,:]
        ttypes2[1,:,:]=types[i,0,:,:]
        ttypes2[2,:,:]=types[i,2,:,:]

        ttypes3=np.zeros((3,2,2))
        ttypes3[0,:,:]=types[i,2,:,:]
        ttypes3[1,:,:]=types[i,1,:,:]
        ttypes3[2,:,:]=types[i,0,:,:]

        ttypes4=np.zeros((3,2,2))
        ttypes4[0,:,:]=types[i,0,:,:]
        ttypes4[1,:,:]=types[i,2,:,:]
        ttypes4[2,:,:]=types[i,1,:,:]
        for j in range (0,4):
            if (types[i,:,:,:]!=-1).any() and (types[j,:,:,:]!=-1).any():
                if (types[j,3:6,:,:]==types[i,0:3,:,:]).all() or (types[j,3:6,:,:]==ttypes).all() or (types[j,3:6,:,:]==ttypes1).all() or (types[j,3:6,:,:]==ttypes2).all() or (types[j,3:6,:,:]==ttypes3).all() or (types[j,3:6,:,:]==ttypes4).all():
                    if np.sum(identical[i,:,0])==0 and np.sum(identical[:,j,0])==0:
                        identical[i,j,0]=1
                if (types[j,6:8,:,:]==types[i,0:2,:,:]).all() or (types[j,6:8,:,:]==ttypes[0:2,:,:]).all() or (types[j,6:8,:,:]==ttypes1[0:2,:,:]).all() or (types[j,6:8,:,:]==ttypes2[0:2,:,:]).all() or (types[j,6:8,:,:]==ttypes3[0:2,:,:]).all() or (types[j,6:8,:,:]==ttypes4[0:2,:,:]).all():
                    if np.sum(identical[i,:,1])==0 and np.sum(identical[:,j,1])==0:
                        identical[i,j,1]=1
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