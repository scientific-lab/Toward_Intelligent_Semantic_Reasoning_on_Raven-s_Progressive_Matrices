import numpy as np
def relation_map(d):
    relationship_two=np.zeros((9,9))
    relationship_three=np.zeros((9,9,9))
    for i in range (0,9):
        for j in range (0,i):
            relationship_two[i,j]=two_ship(d[:,:,i],d[:,:,j])
    #print(relationship_two)
    for ii in range (0,9):
        for jj in range (0,ii):
            for kk in range (0,jj):
                relationship_three[kk,jj,ii]=three_ship(d[:,:,kk],d[:,:,jj],d[:,:,ii])
#     for a in range (1,11):
#         if relationship_two[relationship_two==a].size<3:
#             relationship_two[relationship_two==a]=0
#     for b in range (11,13):
#         if relationship_three[relationship_three==b].size<3:
#             relationship_three[relationship_three==b]=0
    return relationship_two,relationship_three

def relation_map_in(d):
    relationship_two=np.zeros((9,9))
    relationship_three=np.zeros((9,9,9))
    for i in range (0,8):
        for j in range (0,i):
            relationship_two[i,j]=two_ship(d[:,:,i],d[:,:,j])
    #print(relationship_two)
    for ii in range (0,8):
        for jj in range (0,ii):
            for kk in range (0,jj):
                relationship_three[kk,jj,ii]=three_ship(d[:,:,kk],d[:,:,jj],d[:,:,ii])
    return relationship_two,relationship_three

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


def progression(Exist0,n):
    predict1=np.ones((3,3))*-1
    for i in range (0,int(n+1)):
        if i==0:
            predict1=progression_place_template_threebythree(Exist0)
        if i>0:
            predict1=progression_place_template_threebythree(predict1)
    return predict1


def minus(a,b):
    predict1=a-b
    predict1[predict1<0]=0
    return predict1

def plus(a,b):
    predict1=a+b
    predict1[predict1>1]=1
    return predict1

def two_ship(b,a):
    relationship=0
    if (b==a).all():
        relationship=1
    for n in range (0,9): 
        if (b==progression(a,n)).all():
            relationship=n+2
    return relationship



def three_ship(a,b,c):
    relationship=0
    if (c==plus(a,b)).all():
        relationship=11
    if (c==minus(a,b)).all():
        relationship=12
    return relationship

def solve_r2(relationship_two,d):
    solve=0
    c=0
    c1=0
    p=np.ones((3,3,8))*(-1)
    for i in range (0,8):
        p[:,:,i]=predict_2(relationship_two[8,i],i,d)
    for j in range (0,8):
        if (p[:,:,j]!=-1).any():
            c1+=1
            if (p[:,:,j]==d[:,:,8]).all():
                c+=1
    if c1>0:
        if c/c1>0.5:
            solve=1
    return solve
def solve_r3(relationship_three,d):
    solve=0
    c=0
    c1=0
    p=np.ones((3,3,8,8))*(-1)
    for i in range (0,8):
        for j in range (i,8):
            if i!=j:
                p[:,:,i,j]=predict_3(relationship_three[i,j,8],i,j,d)
    for a in range (0,8):
        for b in range (0,8):
            if (p[:,:,a,b]!=-1).any():
                c1+=1
                if (p[:,:,a,b]==d[:,:,8]).all():
                    c+=1
    if c1>0:
        if c/c1>0.5:
            solve=1
    return solve

def solve_r2_return(relationship_two,d):
    solve=0
    c=0
    c1=0
    c2=np.zeros(8)
    p=np.ones((3,3,8))*(-1)
    p1=np.ones((3,3,8))*(-1)
    a=0
    for i in range (0,8):
        p[:,:,i]=predict_2(relationship_two[8,i],i,d)
    for j in range (0,8):
        if (p[:,:,j]!=-1).any():
            c1+=1
            c3=0
            for k in range (0,8):
                if (p[:,:,j]==p1[:,:,k]).all():
                    c2[k]+=1
                    c3=1
            if c3==0:
                p1[:,:,a]=p[:,:,j]
                a+=1
    predict=p1[:,:,np.argmax(c2)]
    return predict
            
def solve_r3_return(relationship_three,d):
    solve=0
    c=0
    c1=0
    c2=np.zeros(8)
    p=np.ones((3,3,8,8))*(-1)
    p1=np.ones((3,3,8))*(-1)
    g=0
    for i in range (0,8):
        for j in range (0,8):
            if i!=j:
                p[:,:,i,j]=predict_3(relationship_three[i,j,8],i,j,d)
    for a in range (0,8):
        for b in range (0,8):
            if (p[:,:,a,b]!=-1).any():
                c1+=1
                c3=0
                for e in range (0,8):
                    if (p[:,:,a,b]==p1[:,:,e]).all():
                        c2[e]+=1
                        c3=1
                if c3==0:
                    if g<8:
                        p1[:,:,g]=p[:,:,a,b]
                        g+=1
                    else:
                        p1[:,:,np.argmin(c2)]=p[:,:,a,b]
                        c2[np.argmin(c2)]=1
    predict=p1[:,:,np.argmax(c2)]          
    return predict

def predict_2(relationship,pos,d):
    p=-1
    if relationship==1:
        p=d[:,:,pos]
    if relationship>=2:
        p=progression(d[:,:,pos],relationship-2) 
    return p

def predict_3(relationship,pos1,pos2,d):
    p=-1
    if relationship==11:
        p=plus(d[:,:,pos1],d[:,:,pos2])
    if relationship==12:
        p=minus(d[:,:,pos1],d[:,:,pos2])  
    return p
    
    
    
    

# relationship_two_30=np.zeros((9,9,30))
# relationship_three_30=np.zeros((9,9,9,30))
# count=np.zeros(30)
# for i in range (0,15000):
#     s=0
#     d=np.load('D:\\zsk\\RAVEN\\data9\\'+str(i)+'.npy')
#     relationship_two,relationship_three=relation_map(d)
#     for i in range (0,30):
#         if (relationship_two_30[:,:,i]==relationship_two).all():
#             if (relationship_three_30[:,:,:,i]==relationship_three).all():
#                 s=1
#                 count[i]+=1
#     if s==0:
#         relationship_two_30[:,:,np.argmin(count)]=relationship_two
#         relationship_three_30[:,:,:,np.argmin(count)]=relationship_three
# np.save('relationship_two_30.npy',relationship_two_30)
# np.save('relationship_three_30.npy',relationship_three_30)
        
    