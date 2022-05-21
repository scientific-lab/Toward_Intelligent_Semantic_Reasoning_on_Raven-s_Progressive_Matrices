import numpy as np
def cut_edge(img):
    area=np.zeros((24,24))
    #img=np.load('380.npy')
    #img=np.load('154.npy')
    #img=np.load('362.npy')
    #img=np.load('382.npy')
    if (img[:,0][10:15]==np.array([48,  8,  0,  8, 48])).all() and (img[23,:][9:14]==np.array([48,  8,  0,  8, 48])).all():
        area1=np.load('area1.npy')
        area[area1==1]=1
    if (img[23,:][10:15]==np.array([48,  8,  0,  8, 48])).all() and (img[:,23][10:15]==np.array([48,  8,  0,  8, 48])).all():
        area2=np.load('area2.npy')
        area[area2==1]=1
    if (img[0,:][10:15]==np.array([48,  8,  0,  8, 48])).all() and (img[:,23][9:14]==np.array([48,  8,  0,  8, 48])).all():
        area3=np.load('area3.npy')
        area[area3==1]=1
    if (img[0,:][9:14]==np.array([48,  8,  0,  8, 48])).all() and (img[:,0][9:14]==np.array([48,  8,  0,  8, 48])).all():
        area4=np.load('area4.npy')
        area[area4==1]=1


    if (img[23,:][9:16]==np.array([0, 0, 0, 0, 0, 0, 0])).all() and (img[:,23][9:16]==np.array([0, 0, 0, 0, 0, 0, 0])).all():
        area1=np.load('area_1.npy')
        area[area1==1]=1
    if (img[0,:][9:16]==np.array([0, 0, 0, 0, 0, 0, 0])).all() and (img[:,23][8:15]==np.array([0, 0, 0, 0, 0, 0, 0])).all():
        area2=np.load('area_2.npy')
        area[area2==1]=1
    if (img[0,:][8:15]==np.array([0, 0, 0, 0, 0, 0, 0])).all() and (img[:,0][8:15]==np.array([0, 0, 0, 0, 0, 0, 0])).all():
        area3=np.load('area_3.npy')
        area[area3==1]=1
    if (img[23,:][8:15]==np.array([0, 0, 0, 0, 0, 0, 0])).all() and (img[:,0][9:16]==np.array([0, 0, 0, 0, 0, 0, 0])).all():
        area4=np.load('area_4.npy')
        area[area4==1]=1
        
    if (img[:,0][10:15]!=np.array([48,8,0,8,48])).any() and (img[:,0][9:14]!=np.array([48,8,0,8,48])).any():
        if (img[0,:][10:15]!=np.array([48,8,0,8,48])).any() and (img[0,:][9:14]!=np.array([48,8,0,8,48])).any():
            if (img[23,:][10:15]!=np.array([48,8,0,8,48])).any() and (img[23,:][9:14]!=np.array([48,8,0,8,48])).any():
                if (img[:,23][10:15]!=np.array([48,8,0,8,48])).any() and (img[:,23][9:14]!=np.array([48,8,0,8,48])).any():
                    
                    if (img[:,0][8:15]!=np.array([0, 0, 0, 0, 0, 0, 0])).any() and (img[:,0][9:16]!=np.array([0, 0, 0, 0, 0, 0, 0])).any():
                        if (img[0,:][8:15]!=np.array([0, 0, 0, 0, 0, 0, 0])).any() and (img[0,:][9:16]!=np.array([0, 0, 0, 0, 0, 0, 0])).any():
                            if (img[23,:][8:15]!=np.array([0, 0, 0, 0, 0, 0, 0])).any() and (img[23,:][9:16]!=np.array([0, 0, 0, 0, 0, 0, 0])).any():
                                if (img[:,23][8:15]!=np.array([0, 0, 0, 0, 0, 0, 0])).any() and (img[:,23][9:16]!=np.array([0, 0, 0, 0, 0, 0, 0])).any():
                                    
                                    if img[:,0][img[:,0]==0].size>0 and img[:,0][img[:,0]==0].size<=5 and img[:,0][img[:,0]==0].size==img[:,0][img[:,0]<255].size:
                                        if img[0,:][img[0,:]==0].size>0 and img[0,:][img[0,:]==0].size<=5 and img[0,:][img[0,:]==0].size==img[0,:][img[0,:]<255].size:
                                            for i in range (0,5):
                                                if img[:,i][img[:,i]==0].size<=5 and img[:,i][img[:,i]==0].size==img[:,i][img[:,i]<255].size: 
                                                    area[:,i][img[:,i]==0]=1
                                                if img[i,:][img[i,:]==0].size<=5 and img[i,:][img[i,:]==0].size==img[i,:][img[i,:]<255].size:
                                                    area[i,:][img[i,:]==0]=1

                                            for i in range (0,np.where(img[0,:]==0)[0][-1]+1):
                                                if img[:,i][img[:,i]==0].size>0:
                                                    k=np.where(img[:,i]==0)[0]
                                                    c=0
                                                    for ii in range (0,k.size-2):
                                                        if k[ii+1]-k[ii]==1:
                                                            c+=1
                                                        else:
                                                            break
                                                    if k[c]+3<24:
                                                        if c>=2 and c<=5 and (img[k[c]+2,i]==255 or img[k[c]+2,i]!=img[k[c]+3,i]):
                                                            area[0:k[c]+1,i]=1
                                            for i in range (0,np.where(img[:,0]==0)[0][-1]+1):
                                                if img[i,:][img[i,:]==0].size>0:
                                                    k=np.where(img[i,:]==0)[0]
                                                    c=0
                                                    for ii in range (0,k.size-2):
                                                        if k[ii+1]-k[ii]==1:
                                                            c+=1
                                                        else:
                                                            break
                                                    if k[c]+3<24:
                                                        if c>=2 and c<=5 and (img[k[c]+2,i]==255 or img[k[c]+2,i]!=img[k[c]+3,i]):
                                                            area[i,0:k[c]+1]=1



                                    if img[:,0][img[:,0]==0].size>0 and img[:,0][img[:,0]==0].size<=5 and img[:,0][img[:,0]==0].size==img[:,0][img[:,0]<255].size:
                                        if img[23,:][img[23,:]==0].size>0 and img[23,:][img[23,:]==0].size<=5 and img[23,:][img[23,:]==0].size==img[23,:][img[23,:]<255].size:
                                            for i in range (0,5):
                                                if img[:,i][img[:,i]==0].size<=5 and img[:,i][img[:,i]==0].size==img[:,i][img[:,i]<255].size: 
                                                    area[:,i][img[:,i]==0]=1
                                            for i in range (19,24):
                                                if img[i,:][img[i,:]==0].size<=5 and img[i,:][img[i,:]==0].size==img[i,:][img[i,:]<255].size:
                                                    area[i,:][img[i,:]==0]=1

                                            for i in range (0,np.where(img[23,:]==0)[0][-1]+1):
                                                if img[:,i][img[:,i]==0].size>0:
                                                    k=np.where(img[:,i]==0)[0]
                                                    c=0
                                                    for ii in range (0,k.size-2):
                                                        if k[-(ii+1)]-k[-(ii+2)]==1:
                                                            c+=1
                                                        else:
                                                            break
                                                    if k[-(c+1)]-2>=0:
                                                        if c>=2 and c<=5 and (img[k[-(c+1)]-1,i]==255 or img[k[-(c+1)]-1,i]!=img[k[-(c+1)]-2,i]):
                                                            area[k[-(c+1)]:24,i]=1
                                            for i in range (np.where(img[:,0]==0)[0][0],24):
                                                if img[i,:][img[i,:]==0].size>0:
                                                    k=np.where(img[i,:]==0)[0]
                                                    c=0
                                                    for ii in range (0,k.size-2):
                                                        if k[ii+1]-k[ii]==1:
                                                            c+=1
                                                        else:
                                                            break
                                                    if k[c]+3<24:
                                                        if c>=2 and c<=5 and (img[i,k[c]+2]==255 or img[i,k[c]+2]!=img[i,k[c]+3]):
                                                            area[i,0:k[c]+1]=1

                                    if img[:,23][img[:,23]==0].size>0 and img[:,23][img[:,23]==0].size<=5 and img[:,23][img[:,23]==0].size==img[:,23][img[:,23]<255].size:
                                        if img[0,:][img[0,:]==0].size>0 and img[0,:][img[0,:]==0].size<=5 and img[0,:][img[0,:]==0].size==img[0,:][img[0,:]<255].size:
                                            for i in range (19,24):
                                                if img[:,i][img[:,i]==0].size<=5 and img[:,i][img[:,i]==0].size==img[:,i][img[:,i]<255].size: 
                                                    area[:,i][img[:,i]==0]=1
                                            for i in range (0,5):
                                                if img[i,:][img[i,:]==0].size<=5 and img[i,:][img[i,:]==0].size==img[i,:][img[i,:]<255].size:
                                                    area[i,:][img[i,:]==0]=1

                                            for i in range (np.where(img[0,:]==0)[0][0],24):
                                                if img[:,i][img[:,i]==0].size>0:
                                                    k=np.where(img[:,i]==0)[0]
                                                    c=0
                                                    for ii in range (0,k.size-2):
                                                        if k[ii+1]-k[ii]==1:
                                                            c+=1
                                                        else:
                                                            break
                                                    if k[c]+3<24:
                                                        if c>=2 and c<=5 and (img[k[c]+2,i]==255 or img[k[c]+2,i]!=img[k[c]+3,i]):
                                                            area[0:k[c]+1,i]=1
                                            for i in range (0,np.where(img[:,23]==0)[0][-1]+1):
                                                if img[i,:][img[i,:]==0].size>0:
                                                    k=np.where(img[i,:]==0)[0]
                                                    c=0
                                                    for ii in range (0,k.size-2):
                                                        if k[-(ii+1)]-k[-(ii+2)]==1:
                                                            c+=1
                                                        else:
                                                            break
                                                    if k[-(c+1)]-2>=0:
                                                        if c>=2 and c<=5 and (img[i,k[-(c+1)]-1]==255 or img[i,k[-(c+1)]-1]!=img[i,k[-(c+1)]-2]):
                                                            area[i,k[-(c+1)]:24]=1



                                    if img[:,23][img[:,23]==0].size>0 and img[:,23][img[:,23]==0].size<=5 and img[:,23][img[:,23]==0].size==img[:,23][img[:,23]<255].size:
                                        if img[23,:][img[23,:]==0].size>0 and img[23,:][img[23,:]==0].size<=5 and img[23,:][img[23,:]==0].size==img[23,:][img[23,:]<255].size:
                                            for i in range (19,24):
                                                if img[:,i][img[:,i]==0].size<=5 and img[:,i][img[:,i]==0].size==img[:,i][img[:,i]<255].size: 
                                                    area[:,i][img[:,i]==0]=1
                                            for i in range (19,24):
                                                if img[i,:][img[i,:]==0].size<=5 and img[i,:][img[i,:]==0].size==img[i,:][img[i,:]<255].size:
                                                    area[i,:][img[i,:]==0]=1

                                            for i in range (np.where(img[23,:]==0)[0][0],24):
                                                if img[:,i][img[:,i]==0].size>0:
                                                    k=np.where(img[:,i]==0)[0]
                                                    c=0
                                                    for ii in range (0,k.size-2):
                                                        if k[-(ii+1)]-k[-(ii+2)]==1:
                                                            c+=1
                                                        else:
                                                            break
                                                    if k[-(c+1)]-2>=0:
                                                        if c>=2 and c<=5 and (img[k[-(c+1)]-1,i]==255 or img[k[-(c+1)]-1,i]!=img[k[-(c+1)]-2,i]):
                                                            area[k[-(c+1)]:24,i]=1

                                            for i in range (np.where(img[:,23]==0)[0][0],24):
                                                if img[i,:][img[i,:]==0].size>0:
                                                    k=np.where(img[i,:]==0)[0]
                                                    c=0
                                                    for ii in range (0,k.size-2):
                                                        if k[-(ii+1)]-k[-(ii+2)]==1:
                                                            c+=1
                                                        else:
                                                            break
                                                    if k[-(c+1)]-2>=0:
                                                        if c>=2 and c<=5 and (img[i,k[-(c+1)]-1]==255 or img[i,k[-(c+1)]-1]!=img[i,k[-(c+1)]-2]):
                                                            area[i,k[-(c+1)]:24]=1
                                                        
                                    if img[0,:][img[0,:]<255].size>0 and img[:,23][img[:,23]<255].size>0:
                                        if img[0,:][img[0,:]==0].size>0 and img[:,23][img[:,23]==0].size>0:
                                            if img[23,:][img[23,:]==0].size==0 or img[:,0][img[:,0]==0].size==0:
                                                a1=np.where(img[0,:]<255)
                                                b1=np.where(img[0,:]>0)
                                                I1=np.intersect1d(a1,b1)
                                                a2=np.where(img[:,23]<255)
                                                b2=np.where(img[:,23]>0)
                                                I2=np.intersect1d(a2,b2)
                                                if I1.size>0 and I2.size>0:


                                                    for i in range (0,23-np.where(img[0,:]<255)[0][0]+1):
                                                        if img[:,23-i][img[:,23-i]<255].size>0:
                                                            a=np.where(img[:,23-i]<255)[0]
                                                            b=np.where(img[:,23-i]>0)[0]
                                                            #a.intersection(b)
                                                            c=np.where(img[:,23-i]==0)[0]
                                                            I=np.intersect1d(a,b)
                                                            if I.size>=2:
                                                                if I[0]==0 and I[1]==1:
                                                                    I=I[1:]
                                                                if I[-1]==23 and I[-2]==22:
                                                                    I=I[:-1]
                                                            if I.size>=1:
                                                                if img[0,23-i]!=0 and img[I[0]+1,23-i]!=255:
                                                                    if I.size>=2:
                                                                        if c[c<I[1]].size>5:
                                                                                I[1]=I[1]-7
                                                                        if I[1]+1<24:
                                                                            area[0:I[1]+1,23-i]=1
                                                                            if img[I[1]+1,23-i]>=250:
                                                                                if I[1]+2<24:
                                                                                    area[0:I[1]+2,23-i]=1
                                                                            if I[1]+3<24:
                                                                                if img[I[1]+2,23-i]>=250:
                                                                                    area[0:I[1]+3,23-i]=1
                                                                else:
                                                                    if I[0]+1<24:
                                                                        area[0:I[0]+1,23-i]=1
                                                                        if img[I[0]+1,23-i]>=250:
                                                                            if I[0]+2<24:
                                                                                area[0:I[0]+2,23-i]=1
                                                                        if I[0]+3<24:
                                                                            if img[I[0]+2,23-i]>=250:
                                                                                area[0:I[0]+3,23-i]=1
                                                                if I.size>=2:
                                                                    if I[1]+1<24:
                                                                        if img[I[1]+1:24,23-i][img[I[1]+1:24,23-i]==0].size==0:
                                                                            if I[-1]+1<24:
                                                                                area[0:I[-1]+1,23-i]=1
                                                            if a.size>0:
                                                                if a[0]+2<24:
                                                                    if a[0]<3 and img[a[0]+1,i]>=250:
                                                                        area[0:a[0]+2,i]=1
                                                                if a[0]+3<24:
                                                                    if a[0]<3 and img[a[0]+2,i]>=250:
                                                                        area[0:a[0]+3,i]=1
                                                            if a.size>1:
                                                                if a[1]+2<24:
                                                                    if a[1]<3 and img[a[1]+1,i]>=250:
                                                                        area[0:a[1]+2,i]=1
                                                                if a[1]+3<24:
                                                                    if a[1]<3 and img[a[1]+2,i]>=250:
                                                                        area[0:a[1]+3,i]=1
                                                    #img[area==1]=255            

                                                    if img[:,23][img[:,23]<255].size>0:
                                                        for i in range (0,np.where(img[:,23]<255)[0][-1]+1):
                                                            if img[i,:][img[i,:]<255].size>0:
                                                                a=np.where(img[i,:]<255)[0]
                                                                b=np.where(img[i,:]>0)[0]
                                                                c=np.where(img[i,:]==0)[0]
                                                                I=np.intersect1d(a,b)
                                                                if I.size>=2:
                                                                    if I[0]==0 and I[1]==1:
                                                                        I=I[1:]
                                                                    if I[-1]==23 and I[-2]==22:
                                                                        I=I[:-1]
                                                                if I.size>=1:
                                                                    if img[i,23]!=0 and img[i,I[-1]-1]!=255:
                                                                        if I.size>=2:
                                                                            if c[c>I[-2]].size>5:
                                                                                I[-2]=I[-2]+7
                                                                            area[i,I[-2]:24]=1
                                                                            if img[i,I[-2]-1]>=250:
                                                                                area[i,I[-2]-1:24]=1
                                                                            if img[i,I[-2]-2]>=250:
                                                                                area[i,I[-2]-2:24]=1
                                                                    else:
                                                                        area[i,I[-1]:24]=1
                                                                        if img[i,I[-1]-1]>=250:
                                                                            area[i,I[-1]-1:24]=1
                                                                        if img[i,I[-1]-2]>=250:
                                                                            area[i,I[-1]-2:24]=1
                                                                    if I.size>=2:
                                                                        if img[i,0:I[-2]][img[i,0:I[-2]]==0].size==0:
                                                                            area[i,I[0]:24]=1
                                                                if a.size>0:
                                                                    if a[-1]>20 and img[i,a[-1]-1]>=250:
                                                                        area[i,a[-1]-1:24]=1
                                                                    if a[-1]>20 and img[i,a[-1]-2]>=250:
                                                                        area[i,a[-1]-2:24]=1
                                                                if a.size>1:
                                                                    if a[-2]>20 and img[i,a[-2]-1]>=250:
                                                                        area[i,a[-2]-1:24]=1
                                                                    if a[-2]>20 and img[i,a[-2]-2]>=250:
                                                                        area[i,a[-2]-1:24]=1


                                    #img[area==1]=255
                                    if img[0,:][img[0,:]<255].size>0 and img[:,0][img[:,0]<255].size>0:
                                        if img[0,:][img[0,:]==0].size>0 and img[:,0][img[:,0]==0].size>0:
                                            if img[23,:][img[23,:]==0].size==0 or img[:,23][img[:,23]==0].size==0:
                                                a1=np.where(img[0,:]<255)
                                                b1=np.where(img[0,:]>0)
                                                I1=np.intersect1d(a1,b1)
                                                a2=np.where(img[:,0]<255)
                                                b2=np.where(img[:,0]>0)
                                                I2=np.intersect1d(a2,b2)
                                                if I1.size>0 and I2.size>0:
                                                    
                                                    for i in range (0,np.where(img[0,:]<255)[0][-1]+1):
                                                        if img[:,i][img[:,i]<255].size>0:
                                                            a=np.where(img[:,i]<255)[0]
                                                            b=np.where(img[:,i]>0)[0]
                                                            c=np.where(img[:,i]==0)[0]
                                                            #a.intersection(b)
                                                            I=np.intersect1d(a,b)
                                                            if I.size>=2:
                                                                if I[0]==0 and I[1]==1:
                                                                    I=I[1:]
                                                                if I[-1]==23 and I[-2]==22:
                                                                    I=I[:-1]
                                                            if I.size>=1:
                                                                if img[0,i]!=0 and img[I[0]+1,i]!=255:
                                                                    if I.size>=2:
                                                                        if c[c<I[1]].size>5:
                                                                                I[1]=I[1]-7
                                                                        if I[1]+1<24:
                                                                            area[0:I[1]+1,i]=1
                                                                            if img[I[1]+1,i]>=250:
                                                                                if I[1]+2<24:
                                                                                    area[0:I[1]+2,i]=1
                                                                            if I[1]+3<24:
                                                                                if img[I[1]+2,i]>=250:
                                                                                    area[0:I[1]+3,i]=1
                                                                else:
                                                                    if I[0]+1<24:
                                                                        area[0:I[0]+1,i]=1
                                                                        if img[I[0]+1,i]>=250:
                                                                            if I[0]+2<24:
                                                                                area[0:I[0]+2,i]=1
                                                                        if I[0]+3<24:
                                                                            if img[I[0]+2,i]>=250:
                                                                                area[0:I[0]+3,i]=1
                                                                if I.size>=2:
                                                                    if I[1]+1<24:
                                                                        if img[I[1]+1:24,i][img[I[1]+1:24,i]==0].size==0:
                                                                            if I[-1]+1<24:
                                                                                area[0:I[-1]+1,i]=1
                                                            if a.size>0:
                                                                if a[0]+2<24:
                                                                    if a[0]<3 and img[a[0]+1,i]>=250:
                                                                        area[0:a[0]+2,i]=1
                                                                if a[0]+3<24:
                                                                    if a[0]<3 and img[a[0]+2,i]>=250:
                                                                        area[0:a[0]+3,i]=1
                                                            if a.size>1:
                                                                if a[1]+2<24:
                                                                    if a[1]<3 and img[a[1]+1,i]>=250:
                                                                        area[0:a[1]+2,i]=1
                                                                if a[1]+3<24:
                                                                    if a[1]<3 and img[a[1]+2,i]>=250:
                                                                        area[0:a[1]+3,i]=1
                                                    #img[area==1]=255            

                                                    if img[:,0][img[:,0]<255].size>0:
                                                        for i in range (0,np.where(img[:,0]<255)[0][-1]+1):
                                                            if img[i,:][img[i,:]<255].size>0:
                                                                a=np.where(img[i,:]<255)[0]
                                                                b=np.where(img[i,:]>0)[0]
                                                                #a.intersection(b)
                                                                c=np.where(img[i,:]==0)[0]
                                                                I=np.intersect1d(a,b)
                                                                if I.size>=2:
                                                                    if I[0]==0 and I[1]==1:
                                                                        I=I[1:]
                                                                    if I[-1]==23 and I[-2]==22:
                                                                        I=I[:-1]
                                                                if I.size>=1:
                                                                    if img[i,0]!=0 and img[i,I[0]+1]!=255:
                                                                        if I.size>=2:
                                                                            if c[c<I[1]].size>5:
                                                                                I[1]=I[1]-7
                                                                            if I[1]+1<24:
                                                                                area[i,0:I[1]+1]=1
                                                                                if img[i,I[1]+1]>=250:
                                                                                    if I[1]+2<24:
                                                                                        area[i,0:I[1]+2]=1
                                                                                if I[1]+3<24:
                                                                                    if img[i,I[1]+2]>=250:
                                                                                        area[i,0:I[1]+3]=1
                                                                    else:
                                                                        if I[0]+1<24:
                                                                            area[i,0:I[0]+1]=1
                                                                            if img[i,I[0]+1]>=250:
                                                                                if I[0]+2<24:
                                                                                    area[i,0:I[0]+2]=1
                                                                            if I[0]+3<24:
                                                                                if img[i,I[0]+2]>=250:
                                                                                    area[i,0:I[0]+3]=1
                                                                    if I.size>=2:
                                                                        if I[1]+1<24:
                                                                            if img[i,I[1]+1:24][img[i,I[1]+1:24]==0].size==0:
                                                                                if I[-1]+1<24:
                                                                                    area[i,0:I[-1]+1]=1
                                                                if a.size>0:
                                                                    if a[0]+2<24:
                                                                        if a[0]<3 and img[i,a[0]+1]>=250:
                                                                            area[i,0:a[0]+2]=1
                                                                    if a[0]+3<24:
                                                                        if a[0]<3 and img[i,a[0]+2]>=250:
                                                                            area[i,0:a[0]+3]=1
                                                                if a.size>1:
                                                                    if a[1]+2<24:
                                                                        if a[1]<3 and img[i,a[1]+1]>=250:
                                                                            area[i,0:a[1]+2]=1
                                                                    if a[1]+3<24:
                                                                        if a[1]<3 and img[i,a[1]+2]>=250:
                                                                            area[i,0:a[1]+3]=1

                                    #img[area==1]=255

                                    if img[23,:][img[23,:]<255].size>0 and img[:,0][img[:,0]<255].size>0:
                                        if img[23,:][img[23,:]==0].size>0 and img[:,0][img[:,0]==0].size>0:
                                            if img[0,:][img[0,:]==0].size==0 or img[:,23][img[:,23]==0].size==0:
                                                a1=np.where(img[23,:]<255)
                                                b1=np.where(img[23,:]>0)
                                                I1=np.intersect1d(a1,b1)
                                                a2=np.where(img[:,0]<255)
                                                b2=np.where(img[:,0]>0)
                                                I2=np.intersect1d(a2,b2)
                                                if I1.size>0 and I2.size>0:
                                                    
                                                    for i in range (0,np.where(img[23,:]<255)[0][-1]+1):
                                                        if img[:,i][img[:,i]<255].size>0:
                                                            a=np.where(img[:,i]<255)[0]
                                                            b=np.where(img[:,i]>0)[0]
                                                            #a.intersection(b)
                                                            c=np.where(img[:,i]==0)[0]
                                                            I=np.intersect1d(a,b)
                                                            if I.size>=2:
                                                                if I[0]==0 and I[1]==1:
                                                                    I=I[1:]
                                                                if I[-1]==23 and I[-2]==22:
                                                                    I=I[:-1]
                                                            if I.size>=1:
                                                                if img[23,i]!=0 and img[I[-1]-1,i]!=255:
                                                                    if I.size>=2:
                                                                        if c[c>I[-2]].size>5:
                                                                            I[-2]=I[-2]+7
                                                                        area[I[-2]:24,i]=1
                                                                        if img[I[-2]-1,i]>=250:
                                                                            area[I[-2]-1:24,i]=1
                                                                        if img[I[-2]-2,i]>=250:
                                                                            area[I[-2]-2:24,i]=1
                                                                else:
                                                                    area[I[-1]:24,i]=1
                                                                    if img[I[-1]-1,i]>=250:
                                                                        area[I[-1]-1:24,i]=1
                                                                    if img[I[-1]-2,i]>=250:
                                                                        area[I[-1]-2:24,i]=1
                                                                if I.size>=2:
                                                                    if img[0:I[-2],i][img[0:I[-2],i]==0].size==0:
                                                                        area[I[0]:24,i]=1
                                                                if a.size>0:
                                                                    if a[-1]>20 and img[a[-1]-1,i]>=250:
                                                                        area[a[-1]-1:24,i]=1
                                                                    if a[-1]>20 and img[a[-1]-2,i]>=250:
                                                                        area[a[-1]-2:24,i]=1
                                                                if a.size>1:
                                                                    if a[-2]>20 and img[a[-2]-1,i]>=250:
                                                                        area[a[-2]-1:24,i]=1
                                                                    if a[-2]>20 and img[a[-2]-2,i]>=250:
                                                                        area[a[-2]-1:24,i]=1
                                                    #img[area==1]=255            

                                                    if img[:,0][img[:,0]<255].size>0:
                                                        for i in range (np.where(img[:,0]<255)[0][0],24):
                                                            if img[i,:][img[i,:]<255].size>0:
                                                                a=np.where(img[i,:]<255)[0]
                                                                b=np.where(img[i,:]>0)[0]
                                                                #a.intersection(b)
                                                                c=np.where(img[i,:]==0)[0]
                                                                I=np.intersect1d(a,b)
                                                                if I.size>=2:
                                                                    if I[0]==0 and I[1]==1:
                                                                        I=I[1:]
                                                                    if I[-1]==23 and I[-2]==22:
                                                                        I=I[:-1]
                                                                if I.size>=1:
                                                                    if img[i,0]!=0 and img[i,I[0]+1]!=255:
                                                                        if I.size>=2:
                                                                            if c[c<I[1]].size>5:
                                                                                I[1]=I[1]-7
                                                                            if I[1]+1<24:
                                                                                if I[1]+1<24:
                                                                                    area[i,0:I[1]+1]=1
                                                                                    if img[i,I[1]+1]>=250:
                                                                                        if I[1]+2<24:
                                                                                            area[i,0:I[1]+2]=1
                                                                                    if I[1]+2<24:
                                                                                        if img[i,I[1]+2]>=250:
                                                                                            if I[1]+3<24:
                                                                                                area[i,0:I[1]+3]=1
                                                                    else:
                                                                        if I[0]+1<24:
                                                                            area[i,0:I[0]+1]=1
                                                                            if img[i,I[0]+1]>=250:
                                                                                if I[0]+2<24:
                                                                                    area[i,0:I[0]+2]=1
                                                                            if I[0]+3<24:
                                                                                if img[i,I[0]+2]>=250:
                                                                                    area[i,0:I[0]+3]=1
                                                                    if I.size>=2:
                                                                        if I[1]+1<24:
                                                                            if img[i,I[1]+1:24][img[i,I[1]+1:24]==0].size==0:
                                                                                if I[-1]+1<24:
                                                                                    area[i,0:I[-1]+1]=1
                                                                if a.size>0:
                                                                    if a[0]+2<24:
                                                                        if a[0]<3 and img[i,a[0]+1]>=250:
                                                                            area[i,0:a[0]+2]=1
                                                                    if a[0]+3<24:
                                                                        if a[0]<3 and img[i,a[0]+2]>=250:
                                                                            area[i,0:a[0]+3]=1
                                                                if a.size>1:
                                                                    if a[1]+2<24:
                                                                        if a[1]<3 and img[i,a[1]+1]>=250:
                                                                            area[i,0:a[1]+2]=1
                                                                    if a[1]+3<24:
                                                                        if a[1]<3 and img[i,a[1]+2]>=250:
                                                                            area[i,0:a[1]+3]=1


                                        #img[area==1]=255

                                    if img[23,:][img[23,:]<255].size>0 and img[:,23][img[:,23]<255].size>0:
                                        if img[23,:][img[23,:]==0].size>0 and img[:,23][img[:,23]==0].size>0:
                                            if img[0,:][img[0,:]==0].size==0 or img[:,0][img[:,0]==0].size==0:
                                                a1=np.where(img[23,:]<255)
                                                b1=np.where(img[23,:]>0)
                                                I1=np.intersect1d(a1,b1)
                                                a2=np.where(img[:,23]<255)
                                                b2=np.where(img[:,23]>0)
                                                I2=np.intersect1d(a2,b2)
                                                if I1.size>0 and I2.size>0:
                                                
                                                    for i in range (np.where(img[23,:]<255)[0][0],24):
                                                        if img[:,i][img[:,i]<255].size>0:
                                                            a=np.where(img[:,i]<255)[0]
                                                            b=np.where(img[:,i]>0)[0]
                                                            #a.intersection(b)
                                                            c=np.where(img[:,i]==0)[0]
                                                            I=np.intersect1d(a,b)
                                                            if I.size>=2:
                                                                if I[0]==0 and I[1]==1:
                                                                    I=I[1:]
                                                                if I[-1]==23 and I[-2]==22:
                                                                    I=I[:-1]
                                                            if I.size>=1:
                                                                if img[23,i]!=0 and img[I[-1]-1,i]!=255:
                                                                    if I.size>=2:
                                                                        if c[c>I[-2]].size>5:
                                                                            I[-2]=I[-2]+7
                                                                        area[I[-2]:24,i]=1
                                                                        if img[I[-2]-1,i]>=250:
                                                                            area[I[-2]-1:24,i]=1
                                                                        if img[I[-2]-2,i]>=250:
                                                                            area[I[-2]-2:24,i]=1
                                                                else:
                                                                    area[I[-1]:24,i]=1
                                                                    if img[I[-1]-1,i]>=250:
                                                                        area[I[-1]-1:24,i]=1
                                                                    if img[I[-1]-2,i]>=250:
                                                                        area[I[-1]-2:24,i]=1
                                                                if I.size>=2:
                                                                    if img[0:I[-2],i][img[0:I[-2],i]==0].size==0:
                                                                        area[I[0]:24,i]=1
                                                                if a.size>0:
                                                                    if a[-1]>20 and img[a[-1]-1,i]>=250:
                                                                        area[a[-1]-1:24,i]=1
                                                                    if a[-1]>20 and img[a[-1]-2,i]>=250:
                                                                        area[a[-1]-2:24,i]=1
                                                                if a.size>1:
                                                                    if a[-2]>20 and img[a[-2]-1,i]>=250:
                                                                        area[a[-2]-1:24,i]=1
                                                                    if a[-2]>20 and img[a[-2]-2,i]>=250:
                                                                        area[a[-2]-1:24,i]=1
                                                    #img[area==1]=255            

                                                    if img[:,23][img[:,23]<255].size>0:
                                                        for i in range (np.where(img[:,23]<255)[0][0],24):
                                                            if img[i,:][img[i,:]<255].size>0:
                                                                a=np.where(img[i,:]<255)[0]
                                                                b=np.where(img[i,:]>0)[0]
                                                                c=np.where(img[i,:]==0)[0]
                                                                I=np.intersect1d(a,b)
                                                                if I.size>=2:
                                                                    if I[0]==0 and I[1]==1:
                                                                        I=I[1:]
                                                                    if I[-1]==23 and I[-2]==22:
                                                                        I=I[:-1]
                                                                if I.size>=1:
                                                                    if img[i,23]!=0 and img[i,I[-1]-1]!=255:
                                                                        if I.size>=2:
                                                                            if c[c>I[-2]].size>5:
                                                                                I[-2]=I[-2]+7
                                                                            area[i,I[-2]:24]=1
                                                                            if img[i,I[-2]-1]>=250:
                                                                                area[i,I[-2]-1:24]=1
                                                                            if img[i,I[-2]-2]>=250:
                                                                                area[i,I[-2]-2:24]=1
                                                                    else:
                                                                        area[i,I[-1]:24]=1
                                                                        if img[i,I[-1]-1]>=250:
                                                                            area[i,I[-1]-1:24]=1
                                                                        if img[i,I[-1]-2]>=250:
                                                                            area[i,I[-1]-2:24]=1
                                                                    if I.size>=2:
                                                                        if img[i,0:I[-2]][img[i,0:I[-2]]==0].size==0:
                                                                            area[i,I[0]:24]=1
                                                                if a.size>0:
                                                                    if a[-1]>20 and img[i,a[-1]-1]>=250:
                                                                        area[i,a[-1]-1:24]=1
                                                                    if a[-1]>20 and img[i,a[-1]-2]>=250:
                                                                        area[i,a[-1]-2:24]=1
                                                                if a.size>1:
                                                                    if a[-2]>20 and img[i,a[-2]-1]>=250:
                                                                        area[i,a[-2]-1:24]=1
                                                                    if a[-2]>20 and img[i,a[-2]-2]>=250:
                                                                        area[i,a[-2]-1:24]=1

    img[area==1]=255
    return img,area