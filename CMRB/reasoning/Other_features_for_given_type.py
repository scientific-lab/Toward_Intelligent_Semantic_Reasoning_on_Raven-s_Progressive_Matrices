import numpy as np
def Type_specific_lists(Type,Angle,Color,Size,Candidate):
    s=Angle[:,:,0].size
    s1=Angle[:,:,0].shape[0]
    Angle_types=-100*np.ones((s,16))
    Color_types=-100*np.ones((s,16))
    Size_types=-100*np.ones((s,16))
    Place_types=-100*np.ones((s,16,s1,s1))
    Type_types=-100*np.ones((4,4))
    if Type[:,:,0][Type[:,:,0]!=-1].size==Type[:,:,1][Type[:,:,1]!=-1].size==Type[:,:,2][Type[:,:,2]!=-1].size:
        if Type[:,:,3][Type[:,:,3]!=-1].size==Type[:,:,4][Type[:,:,4]!=-1].size==Type[:,:,5][Type[:,:,5]!=-1].size:
            if (np.sort(Type[:,:,0][Type[:,:,0]!=-1])==np.sort(Type[:,:,1][Type[:,:,1]!=-1])).all() and (np.sort(Type[:,:,1][Type[:,:,1]!=-1])==np.sort(Type[:,:,2][Type[:,:,2]!=-1])).all():
                if (np.sort(Type[:,:,3][Type[:,:,3]!=-1])==np.sort(Type[:,:,4][Type[:,:,4]!=-1])).all() and (np.sort(Type[:,:,4][Type[:,:,4]!=-1])==np.sort(Type[:,:,5][Type[:,:,5]!=-1])).all():
                    list_candidate=[]
                    for i in range (8,16):
                        if np.sort(Type[:,:,7][Type[:,:,7]!=-1]).size==np.sort(Type[:,:,i][Type[:,:,i]!=-1]).size:
                            if (np.sort(Type[:,:,7][Type[:,:,7]!=-1])!=np.sort(Type[:,:,i][Type[:,:,i]!=-1])).any():
                                Candidate[i-8]-=1
                            else:
                                list_candidate.append(i)
                        else:
                            Candidate[i-8]-=1
                    Type_types=np.ones((max(Type[:,:,0][Type[:,:,0]!=-1].size,Type[:,:,3][Type[:,:,3]!=-1].size,Type[:,:,6][Type[:,:,6]!=-1].size),3))*(-1)
                    for r in (0,3,6):
                        for T in range (0,Type[:,:,r][Type[:,:,r]!=-1].size):
                            Type_types[T,int(r/3)]=Type[:,:,r][Type[:,:,r]!=-1][T]
    #                     reoccur=0
    #                     for i in range (0,3):
    #                         for j in range (0,Type_types[:,0].size):
    #                             if reoccur<Type_types[:,i][Type_types[:,i]==Type_types[j,i]].size:
    #                                 reoccur=Type_types[:,i][Type_types[:,i]==Type_types[j,i]].size
    #                     Angle_types=np.ones((4,8,reoccur))*(-1)
    #                     Color_types=np.ones((4,8,reoccur))*(-1)
    #                     Size_types=np.ones((4,8,reoccur))*(-1)
    #                     Place_types=np.ones((4,8,2,2,reoccur))*(-1)
                    Angle_types=np.ones((s,16))*(-1)
                    Color_types=np.ones((s,16))*(-1)
                    Size_types=np.ones((s,16))*(-1)
                    Place_types=np.ones((s,16,s1,s1))*(-1)
                    for r in range (0,16):
                        if r<3:
                            for T in range (0,Type[:,:,0][Type[:,:,0]!=-1].size):
                                if np.where(Type[:,:,r]== Type_types[T,0])[0].size==1:
                                    Angle_types[T,r]=Angle[:,:,r][np.where(Type[:,:,r]== Type_types[T,0])]
                                    Color_types[T,r]=Color[:,:,r][np.where(Type[:,:,r]== Type_types[T,0])]
                                    Size_types[T,r]=Size[:,:,r][np.where(Type[:,:,r]== Type_types[T,0])]
                                    Place_types[T,r,np.where(Type[:,:,r]== Type_types[T,0])[0][0],np.where(Type[:,:,r]== Type_types[T,0])[1][0]]=1
                                else:
                                    TT=np.where(Type_types[:,0]==Type_types[T,0])[0]
                                    #print(TT)
                                    #print(np.where(Type[:,:,r]== Type_types[T,1])[0].size)
                                    orders_all=np.zeros((np.where(Type[:,:,r]== Type_types[T,0])[0].size,np.where(Type[:,:,r]== Type_types[T,0])[0].size,2))
                                    orders=np.zeros((3,np.where(Type[:,:,r]== Type_types[T,0])[0].size))
                                    for i in range (0,np.where(Type[:,:,r]== Type_types[T,0])[0].size):
                                        orders[0,i]=i
                                    angles_all=np.zeros((3,np.where(Type[:,:,r]== Type_types[T,0])[0].size))
                                    color_all=np.zeros((3,np.where(Type[:,:,r]== Type_types[T,0])[0].size))
                                    size_all=np.zeros((3,np.where(Type[:,:,r]== Type_types[T,0])[0].size))
                                    place_all=np.zeros((3,s1,s1,np.where(Type[:,:,r]== Type_types[T,0])[0].size))
                                    #print(angles_all.shape)
                                    for i in range (0,np.where(Type[:,:,r]== Type_types[T,0])[0].size):
                                        for rr in range (0,3):
                                            if np.where(Type[:,:,rr]== Type_types[T,0])[0].size>0:
                                                if i<np.where(Type[:,:,rr]== Type_types[T,0])[0].size:
                                                    angles_all[rr,i]=Angle[np.where(Type[:,:,rr]== Type_types[T,0])[0][i],np.where(Type[:,:,rr]== Type_types[T,0])[1][i],rr]
                                                    color_all[rr,i]=Color[np.where(Type[:,:,rr]== Type_types[T,0])[0][i],np.where(Type[:,:,rr]== Type_types[T,0])[1][i],rr]
                                                    size_all[rr,i]=Size[np.where(Type[:,:,rr]== Type_types[T,0])[0][i],np.where(Type[:,:,rr]== Type_types[T,0])[1][i],rr]
                                                    place_all[rr-3,np.where(Type[:,:,rr]== Type_types[T,0])[0][i],np.where(Type[:,:,rr]== Type_types[T,0])[1][i],i]=1
                                        for j in range (0,np.where(Type[:,:,r]== Type_types[T,0])[0].size):
                                            if angles_all[0,j]==angles_all[1,i]:
                                                orders_all[i,j,0]+=1
                                            if angles_all[0,j]==angles_all[2,i]:
                                                orders_all[i,j,1]+=1

                                            if color_all[0,j]==color_all[1,i]:
                                                orders_all[i,j,0]+=1
                                            if color_all[0,j]==color_all[2,i]:
                                                orders_all[i,j,1]+=1

                                            if size_all[0,j]==size_all[1,i]:
                                                orders_all[i,j,0]+=1
                                            if size_all[0,j]==size_all[2,i]:
                                                orders_all[i,j,1]+=1

                                            if (place_all[0,:,:,j]==place_all[1,:,:,i]).all():
                                                orders_all[i,j,0]+=1
                                            if (place_all[0,:,:,j]==place_all[2,:,:,i]).all():
                                                orders_all[i,j,1]+=1

                                    for a in range (0,2):
                                        k=[]
                                        for i in range (0,np.where(Type[:,:,r]== Type_types[T,0])[0].size):
                                            if np.argmax(orders_all[:,i,a]) not in k:
                                                k.append(np.argmax(orders_all[:,i,a]))
                                                orders[a+1,np.argmax(orders_all[:,i,a])]=i
                                            else:
                                                l=np.arange(np.where(Type[:,:,r]== Type_types[T,0])[0].size)
                                                orders_all_e=orders_all
                                                orders_all_e[k,i,a]=0
                                                orders[a+1,np.argmax(orders_all_e[:,i,a])]
                                    for i in range (0,np.where(Type[:,:,r]== Type_types[T,0])[0].size):
                                        Angle_types[TT[i],r]=Angle[np.where(Type[:,:,r]== Type_types[T,0])[0][int(orders[r,i])],np.where(Type[:,:,r]== Type_types[T,0])[1][int(orders[r,i])],r]
                                        Color_types[TT[i],r]=Color[np.where(Type[:,:,r]== Type_types[T,0])[0][int(orders[r,i])],np.where(Type[:,:,r]== Type_types[T,0])[1][int(orders[r,i])],r]
                                        #print(TT[i])
                                        Size_types[TT[i],r]=Size[np.where(Type[:,:,r]== Type_types[T,0])[0][int(orders[r,i])],np.where(Type[:,:,r]== Type_types[T,0])[1][int(orders[r,i])],r]
                                        #print(TT[i])
                                        #print(Size[np.where(Type[:,:,r]== Type_types[T,0])[0][int(orders[r,i])],np.where(Type[:,:,r]== Type_types[T,0])[1][int(orders[r,i])],r])
                                        Place_types[TT[i],r,np.where(Type[:,:,r]== Type_types[T,0])[0][int(orders[r,i])],np.where(Type[:,:,r]== Type_types[T,0])[1][int(orders[r,i])]]=1
    #                                         Angle_types[T,r,i]=Angle[np.where(Type[:,:,r]== Type_types[T,0])[0][i],np.where(Type[:,:,r]== Type_types[T,0])[1][i],r]
    #                                         Color_types[T,r,i]=Color[np.where(Type[:,:,r]== Type_types[T,0])[0][i],np.where(Type[:,:,r]== Type_types[T,0])[1][i],r]
    #                                         Size_types[T,r,i]=Size[np.where(Type[:,:,r]== Type_types[T,0])[0][i],np.where(Type[:,:,r]== Type_types[T,0])[1][i],r]
    #                                         Place_types[T,r,np.where(Type[:,:,r]== Type_types[T,0])[0][i],np.where(Type[:,:,r]== Type_types[T,0])[1][i],i]=1
                        if r>=3 and r<6:
                            for T in range (0,Type[:,:,3][Type[:,:,3]!=-1].size):
                                if np.where(Type[:,:,r]== Type_types[T,1])[0].size==1:
                                    Angle_types[T,r]=Angle[:,:,r][np.where(Type[:,:,r]== Type_types[T,1])]
                                    Color_types[T,r]=Color[:,:,r][np.where(Type[:,:,r]== Type_types[T,1])]
                                    Size_types[T,r]=Size[:,:,r][np.where(Type[:,:,r]== Type_types[T,1])]
                                    Place_types[T,r,np.where(Type[:,:,r]== Type_types[T,1])[0][0],np.where(Type[:,:,r]== Type_types[T,1])[1][0]]=1
                                else:
                                    TT=np.where(Type_types[:,1]==Type_types[T,1])[0]
                                    #print(TT)
                                    #print(np.where(Type[:,:,r]== Type_types[T,1])[0].size)
                                    orders_all=np.zeros((np.where(Type[:,:,r]== Type_types[T,1])[0].size,np.where(Type[:,:,r]== Type_types[T,1])[0].size,2))
                                    orders=np.zeros((3,np.where(Type[:,:,r]== Type_types[T,1])[0].size))
                                    for i in range (0,np.where(Type[:,:,r]== Type_types[T,1])[0].size):
                                        orders[0,i]=i
                                    angles_all=np.zeros((3,np.where(Type[:,:,r]== Type_types[T,1])[0].size))
                                    color_all=np.zeros((3,np.where(Type[:,:,r]== Type_types[T,1])[0].size))
                                    size_all=np.zeros((3,np.where(Type[:,:,r]== Type_types[T,1])[0].size))
                                    place_all=np.zeros((3,s1,s1,np.where(Type[:,:,r]== Type_types[T,1])[0].size))
                                    #print(angles_all.shape)
                                    for i in range (0,np.where(Type[:,:,r]== Type_types[T,1])[0].size):
                                        for rr in range (3,6):
                                            if np.where(Type[:,:,rr]== Type_types[T,1])[0].size>0:
                                                if i<np.where(Type[:,:,rr]== Type_types[T,1])[0].size:
                                                    angles_all[rr-3,i]=Angle[np.where(Type[:,:,rr]== Type_types[T,1])[0][i],np.where(Type[:,:,rr]== Type_types[T,1])[1][i],rr]
                                                    color_all[rr-3,i]=Color[np.where(Type[:,:,rr]== Type_types[T,1])[0][i],np.where(Type[:,:,rr]== Type_types[T,1])[1][i],rr]
                                                    size_all[rr-3,i]=Size[np.where(Type[:,:,rr]== Type_types[T,1])[0][i],np.where(Type[:,:,rr]== Type_types[T,1])[1][i],rr]
                                                    place_all[rr-3,np.where(Type[:,:,rr]== Type_types[T,1])[0][i],np.where(Type[:,:,rr]== Type_types[T,1])[1][i],i]=1
                                        for j in range (0,np.where(Type[:,:,r]== Type_types[T,1])[0].size):
                                            if angles_all[0,j]==angles_all[1,i]:
                                                orders_all[i,j,0]+=1
                                            if angles_all[0,j]==angles_all[2,i]:
                                                orders_all[i,j,1]+=1

                                            if color_all[0,j]==color_all[1,i]:
                                                orders_all[i,j,0]+=1
                                            if color_all[0,j]==color_all[2,i]:
                                                orders_all[i,j,1]+=1

                                            if size_all[0,j]==size_all[1,i]:
                                                orders_all[i,j,0]+=1
                                            if size_all[0,j]==size_all[2,i]:
                                                orders_all[i,j,1]+=1

                                            if (place_all[0,:,:,j]==place_all[1,:,:,i]).all():
                                                orders_all[i,j,0]+=1
                                            if (place_all[0,:,:,j]==place_all[2,:,:,i]).all():
                                                orders_all[i,j,1]+=1

                                    for a in range (0,2):
                                        k=[]
                                        for i in range (0,np.where(Type[:,:,r]== Type_types[T,1])[0].size):
                                            if np.argmax(orders_all[:,i,a]) not in k:
                                                k.append(np.argmax(orders_all[:,i,a]))
                                                orders[a+1,np.argmax(orders_all[:,i,a])]=i
                                            else:
                                                l=np.arange(np.where(Type[:,:,r]== Type_types[T,1])[0].size)
                                                orders_all_e=orders_all
                                                orders_all_e[k,i,a]=0
                                                orders[a+1,np.argmax(orders_all_e[:,i,a])]
                                    for i in range (0,np.where(Type[:,:,r]== Type_types[T,1])[0].size):
                                        Angle_types[TT[i],r]=Angle[np.where(Type[:,:,r]== Type_types[T,1])[0][int(orders[r-3,i])],np.where(Type[:,:,r]== Type_types[T,1])[1][int(orders[r-3,i])],r]
                                        Color_types[TT[i],r]=Color[np.where(Type[:,:,r]== Type_types[T,1])[0][int(orders[r-3,i])],np.where(Type[:,:,r]== Type_types[T,1])[1][int(orders[r-3,i])],r]
                                        Size_types[TT[i],r]=Size[np.where(Type[:,:,r]== Type_types[T,1])[0][int(orders[r-3,i])],np.where(Type[:,:,r]== Type_types[T,1])[1][int(orders[r-3,i])],r]
                                        Place_types[TT[i],r,np.where(Type[:,:,r]== Type_types[T,1])[0][int(orders[r-3,i])],np.where(Type[:,:,r]== Type_types[T,1])[1][int(orders[r-3,i])]]=1




                                    #for i in range (0,np.where(Type[:,:,r]== Type_types[T,1])[0].size):
    #                                         Angle_types[T,r,i]=Angle[np.where(Type[:,:,r]== Type_types[T,1])[0][i],np.where(Type[:,:,r]== Type_types[T,1])[1][i],r]
    #                                         Color_types[T,r,i]=Color[np.where(Type[:,:,r]== Type_types[T,1])[0][i],np.where(Type[:,:,r]== Type_types[T,1])[1][i],r]
    #                                         Size_types[T,r,i]=Size[np.where(Type[:,:,r]== Type_types[T,1])[0][i],np.where(Type[:,:,r]== Type_types[T,1])[1][i],r]
    #                                         Place_types[T,r,np.where(Type[:,:,r]== Type_types[T,1])[0][i],np.where(Type[:,:,r]== Type_types[T,1])[1][i],i]=1
                                        #print(np.where(Type[:,:,r]== Type_types[T,1]))
                        if r>=6:
                            for T in range (0,Type[:,:,6][Type[:,:,6]!=-1].size):
                                if r>=8 and np.where(Type[:,:,r]== Type_types[T,2])[0].size==0:
                                    Candidate[r-8]-=1
                                if np.where(Type[:,:,r]== Type_types[T,2])[0].size==1 and (r<8 or r in list_candidate):
                                    Angle_types[T,r]=Angle[:,:,r][np.where(Type[:,:,r]== Type_types[T,2])]
                                    Color_types[T,r]=Color[:,:,r][np.where(Type[:,:,r]== Type_types[T,2])]
                                    Size_types[T,r]=Size[:,:,r][np.where(Type[:,:,r]== Type_types[T,2])]
                                    Place_types[T,r,np.where(Type[:,:,r]== Type_types[T,2])[0][0],np.where(Type[:,:,r]== Type_types[T,2])[1][0]]=1
                                if np.where(Type[:,:,r]== Type_types[T,2])[0].size>1 and np.where(Type[:,:,r]== Type_types[T,2])[0].size==np.where(Type[:,:,6]== Type_types[T,2])[0].size:
                                    TT=np.where(Type_types[:,2]==Type_types[T,2])[0]
                                    #print(np.where(Type[:,:,r]== Type_types[T,1])[0].size)
                                    orders_all=np.zeros((np.where(Type[:,:,r]== Type_types[T,2])[0].size,np.where(Type[:,:,r]== Type_types[T,2])[0].size))
                                    orders=np.zeros((2,np.where(Type[:,:,r]== Type_types[T,2])[0].size))
                                    for i in range (0,np.where(Type[:,:,r]== Type_types[T,2])[0].size):
                                        orders[0,i]=i
                                    angles_all=np.zeros((3,np.where(Type[:,:,r]== Type_types[T,2])[0].size))
                                    color_all=np.zeros((3,np.where(Type[:,:,r]== Type_types[T,2])[0].size))
                                    size_all=np.zeros((3,np.where(Type[:,:,r]== Type_types[T,2])[0].size))
                                    place_all=np.zeros((3,s1,s1,np.where(Type[:,:,r]== Type_types[T,2])[0].size))
                                    #print(angles_all.shape)
                                    for i in range (0,np.where(Type[:,:,r]== Type_types[T,2])[0].size):
                                        for rr in range (6,8):
                                            if np.where(Type[:,:,rr]== Type_types[T,2])[0].size>0:
                                                if i<np.where(Type[:,:,rr]== Type_types[T,2])[0].size:
                                                    angles_all[rr-6,i]=Angle[np.where(Type[:,:,rr]== Type_types[T,2])[0][i],np.where(Type[:,:,rr]== Type_types[T,2])[1][i],rr]
                                                    color_all[rr-6,i]=Color[np.where(Type[:,:,rr]== Type_types[T,2])[0][i],np.where(Type[:,:,rr]== Type_types[T,2])[1][i],rr]
                                                    size_all[rr-6,i]=Size[np.where(Type[:,:,rr]== Type_types[T,2])[0][i],np.where(Type[:,:,rr]== Type_types[T,2])[1][i],rr]
                                                    place_all[rr-6,np.where(Type[:,:,rr]== Type_types[T,2])[0][i],np.where(Type[:,:,rr]== Type_types[T,2])[1][i],i]=1
                                        for j in range (0,np.where(Type[:,:,r]== Type_types[T,2])[0].size):
                                            if angles_all[0,j]==angles_all[1,i]:
                                                orders_all[i,j]+=1

                                            if color_all[0,j]==color_all[1,i]:
                                                orders_all[i,j]+=1

                                            if size_all[0,j]==size_all[1,i]:
                                                orders_all[i,j]+=1

                                            if (place_all[0,:,:,j]==place_all[1,:,:,i]).all():
                                                orders_all[i,j]+=1

                                    a=0
                                    k=[]
                                    for i in range (0,np.where(Type[:,:,r]== Type_types[T,2])[0].size):
                                        if np.argmax(orders_all[:,i]) not in k:
                                            k.append(np.argmax(orders_all[:,i]))
                                            orders[a+1,np.argmax(orders_all[:,i])]=i
                                        else:
                                            l=np.arange(np.where(Type[:,:,r]== Type_types[T,2])[0].size)
                                            orders_all_e=orders_all
                                            orders_all_e[k,i]=0
                                            orders[a+1,np.argmax(orders_all_e[:,i])]

                                    if r<8:

                                        for i in range (0,np.where(Type[:,:,r]== Type_types[T,2])[0].size):
                                            Angle_types[TT[i],r]=Angle[np.where(Type[:,:,r]== Type_types[T,2])[0][int(orders[r-6,i])],np.where(Type[:,:,r]== Type_types[T,2])[1][int(orders[r-6,i])],r]
                                            Color_types[TT[i],r]=Color[np.where(Type[:,:,r]== Type_types[T,2])[0][int(orders[r-6,i])],np.where(Type[:,:,r]== Type_types[T,2])[1][int(orders[r-6,i])],r]
                                            Size_types[TT[i],r]=Size[np.where(Type[:,:,r]== Type_types[T,2])[0][int(orders[r-6,i])],np.where(Type[:,:,r]== Type_types[T,2])[1][int(orders[r-6,i])],r]
                                            Place_types[TT[i],r,np.where(Type[:,:,r]== Type_types[T,2])[0][int(orders[r-6,i])],np.where(Type[:,:,r]== Type_types[T,2])[1][int(orders[r-6,i])]]=1
                                    for i in range (0,np.where(Type[:,:,r]== Type_types[T,2])[0].size):
                                        for rr in list_candidate:
                                            TT=np.where(Type_types[:,2]==Type_types[T,2])[0]
                                            orders_all=np.zeros((np.where(Type[:,:,r]== Type_types[T,2])[0].size,np.where(Type[:,:,r]== Type_types[T,2])[0].size))
                                            orders=np.zeros((2,np.where(Type[:,:,r]== Type_types[T,2])[0].size))
                                            if np.where(Type[:,:,rr]== Type_types[T,2])[0].size>0:
                                                if i<np.where(Type[:,:,rr]== Type_types[T,2])[0].size:
                                                    angles_all[2,i]=Angle[np.where(Type[:,:,rr]== Type_types[T,2])[0][i],np.where(Type[:,:,rr]== Type_types[T,2])[1][i],rr]
                                                    color_all[2,i]=Color[np.where(Type[:,:,rr]== Type_types[T,2])[0][i],np.where(Type[:,:,rr]== Type_types[T,2])[1][i],rr]
                                                    size_all[2,i]=Size[np.where(Type[:,:,rr]== Type_types[T,2])[0][i],np.where(Type[:,:,rr]== Type_types[T,2])[1][i],rr]
                                                    place_all[2,np.where(Type[:,:,rr]== Type_types[T,2])[0][i],np.where(Type[:,:,rr]== Type_types[T,2])[1][i],i]=1
                                            for i in range (0,np.where(Type[:,:,r]== Type_types[T,2])[0].size):
                                                for j in range (0,np.where(Type[:,:,r]== Type_types[T,2])[0].size):
                                                        if angles_all[0,j]==angles_all[2,i]:
                                                            orders_all[i,j]+=1

                                                        if color_all[0,j]==color_all[2,i]:
                                                            orders_all[i,j]+=1

                                                        if size_all[0,j]==size_all[2,i]:
                                                            orders_all[i,j]+=1

                                                        if (place_all[0,:,:,j]==place_all[2,:,:,i]).all():
                                                            orders_all[i,j]+=1

                                            a=1
                                            k=[]
                                            for i in range (0,np.where(Type[:,:,r]== Type_types[T,2])[0].size):
                                                if np.argmax(orders_all[:,i]) not in k:
                                                    k.append(np.argmax(orders_all[:,i]))
                                                    orders[a,np.argmax(orders_all[:,i])]=i
                                                else:
                                                    l=np.arange(np.where(Type[:,:,r]== Type_types[T,2])[0].size)
                                                    orders_all_e=orders_all
                                                    orders_all_e[k,i]=0
                                                    orders[a,np.argmax(orders_all_e[:,i])]
                                            if np.where(Type[:,:,rr]== Type_types[T,2])[0].size>0:
                                                Angle_types[TT[i],rr]=Angle[np.where(Type[:,:,rr]== Type_types[T,2])[0][int(orders[1,i])],np.where(Type[:,:,rr]== Type_types[T,2])[1][int(orders[1,i])],rr]
                                                Color_types[TT[i],rr]=Color[np.where(Type[:,:,rr]== Type_types[T,2])[0][int(orders[1,i])],np.where(Type[:,:,rr]== Type_types[T,2])[1][int(orders[1,i])],rr]
                                                Size_types[TT[i],rr]=Size[np.where(Type[:,:,rr]== Type_types[T,2])[0][int(orders[1,i])],np.where(Type[:,:,rr]== Type_types[T,2])[1][int(orders[1,i])],rr]
                                                Place_types[TT[i],rr,np.where(Type[:,:,rr]== Type_types[T,2])[0][int(orders[1,i])],np.where(Type[:,:,rr]== Type_types[T,2])[1][int(orders[1,i])]]=1
    return Angle_types,Color_types,Size_types,Place_types,Type_types,Candidate