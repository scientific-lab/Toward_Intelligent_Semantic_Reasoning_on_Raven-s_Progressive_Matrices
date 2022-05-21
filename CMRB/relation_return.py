import numpy as np
def relation_map(d):
    relationship_two=np.zeros((9,9))
    relationship_three=np.zeros((9,9,9))
    for i in range (0,9):
        for j in range (0,i):
            relationship_two[i,j]=two_ship(d[i],d[j])
    for ii in range (0,9):
        for jj in range (0,ii):
            for kk in range (0,jj):
                relationship_three[kk,jj,ii]=three_ship(d[kk],d[jj],d[ii])
#     for a in range (1,20):
#         if relationship_two[relationship_two==a].size<3:
#             relationship_two[relationship_two==a]=0
#     for b in range (22,25):
#         if relationship_three[relationship_three==b].size<3:
#             relationship_three[relationship_three==b]=0
    return relationship_two,relationship_three
def relation_map_in(d):
    relationship_two=np.zeros((9,9))
    relationship_three=np.zeros((9,9,9))
    for i in range (0,8):
        for j in range (0,i):
            relationship_two[i,j]=two_ship(d[i],d[j])
    for ii in range (0,8):
        for jj in range (0,ii):
            for kk in range (0,jj):
                relationship_three[kk,jj,ii]=three_ship(d[kk],d[jj],d[ii])
    return relationship_two,relationship_three
def two_ship(b,a):
    relationship=0
    if b-a==0:
        relationship=1
    if b-a==1:
        relationship=2
    if b-a==2:
        relationship=3
    if b-a==3:
        relationship=4
    if b-a==4:
        relationship=5
    if b-a==5:
        relationship=6
    if b-a==6:
        relationship=7
    if b-a==7:
        relationship=8
    if b-a==8:
        relationship=9
    if b-a==9:
        relationship=10
    if b-a==-1:
        relationship=11
    if b-a==-2:
        relationship=12
    if b-a==-3:
        relationship=13
    if b-a==-4:
        relationship=14
    if b-a==-5:
        relationship=15
    if b-a==-6:
        relationship=16
    if b-a==-7:
        relationship=17
    if b-a==-8:
        relationship=18
    if b-a==-9:
        relationship=19
    return relationship


def three_ship(a,b,c):
    relationship=0
    if a+b==c:
        relationship=20
    if a-b==c:
        relationship=21
    if a+b+1==c:
        relationship=22
    if a-b-1==c:
        relationship=23
    if a+b+2==c:
        relationship=24
    if a-b-2==c:
        relationship=25
#     if a+b==c and a-b==c:
#         relationship=26
    return relationship

def solve_r2(relationship_two,d):
    solve=0
    p=np.ones(8)*(-1)
    for i in range (0,8):
        p[i]=predict_2(relationship_two[8,i],i,d)
    if p[p!=-1].size>0:
        if (p[p!=-1]==d[8])[(p[p!=-1]==d[8])==1].size/p[p!=-1].size>0.5:
            solve=1
    return solve
def solve_r3(relationship_three,d):
    solve=0
    p=np.ones((8,8))*(-1)
    for i in range (0,8):
        for j in range (0,8):
            if i!=j:
                p[i,j]=predict_3(relationship_three[i,j,8],i,j,d)
    if p[p!=-1].size>0:
        if (p[p!=-1]==d[8])[(p[p!=-1]==d[8])==1].size/p[p!=-1].size>0.5:
            solve=1
    return solve
    
def predict_2(relationship,pos,d):
    p=-1
    if relationship==1:
        p=d[pos]
    if relationship==2:
        p=d[pos]+1
    if relationship==3:
        p=d[pos]+2
    if relationship==4:
        p=d[pos]+3
    if relationship==5:
        p=d[pos]+4
    if relationship==6:
        p=d[pos]+5
    if relationship==7:
        p=d[pos]+6
    if relationship==8:
        p=d[pos]+7
    if relationship==9:
        p=d[pos]+8
    if relationship==10:
        p=d[pos]+9
    if relationship==11:
        p=d[pos]-1
    if relationship==12:
        p=d[pos]-2
    if relationship==13:
        p=d[pos]-3
    if relationship==14:
        p=d[pos]-4
    if relationship==15:
        p=d[pos]-5
    if relationship==16:
        p=d[pos]-6
    if relationship==17:
        p=d[pos]-7
    if relationship==18:
        p=d[pos]-8
    if relationship==19:
        p=d[pos]-9
    return p

def predict_3(relationship,pos1,pos2,d):
    p=-1
    if relationship==20:
        p=d[pos1]+d[pos2]
    if relationship==21:
        p=d[pos1]-d[pos2]
    if relationship==22:
        p=d[pos1]+d[pos2]+1
    if relationship==23:
        p=d[pos1]-d[pos2]-1
    if relationship==24:
        p=d[pos1]+d[pos2]+2
    if relationship==25:
        p=d[pos1]-d[pos2]-2
#     if relationship==26:
#         p=d[pos1]+d[pos2]
    return p
    
def solve_r2_return(relationship_two,d):
    solve=0
    p=np.ones(8)*(-1)
    pmax=-1
    for i in range (0,8):
        p[i]=predict_2(relationship_two[8,i],i,d)
    if p[p>=0].size>0:
        pp=p[p>=0].tolist()
        for w in range (0,p[p>=0].size):
            pp[w]=int(pp[w])
            #print(p[p!=-1][w])
        counts = np.bincount(pp)
        pmax=np.argmax(counts)
    return pmax

def solve_r3_return(relationship_three,d):
    solve=0
    p=np.ones((8,8))*(-1)
    pmax=-1
    for i in range (0,8):
        for j in range (0,8):
            if i!=j:
                p[i,j]=predict_3(relationship_three[i,j,8],i,j,d)
    if p[p>=0].size>0:
        pp=p[p>=0].tolist()
        for w in range (0,p[p>=0].size):
            pp[w]=int(pp[w])
        counts = np.bincount(pp)
        pmax=np.argmax(counts)
    return pmax    
    
    

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
        
    