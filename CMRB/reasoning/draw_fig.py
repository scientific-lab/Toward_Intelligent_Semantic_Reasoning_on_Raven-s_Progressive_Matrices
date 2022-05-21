import numpy as np
def pre_draw(Exist_predict,Type_predict,Color_predict,Size_predict,Angle_predict,Type_template,Type_types,Color_types_predict,Size_types_predict,Angle_types_predict,Place_predict,Place_types_predict):
    s=Color_types_predict.size
    if Exist_predict<=0:
        Exist_predict=np.random.randint(0,s,1)
    Exist_predict=int(Exist_predict)
    att=np.zeros((Exist_predict,29))
    if Type_predict>=0:
        att[:,int(Type_predict-1)]=1
    if Color_predict>=0:
        att[:,int(5+Color_predict)]=1
    if Size_predict>=0:
        att[:,int(15+Size_predict)]=1
    if Angle_predict>=0:
        att[:,int(21+Angle_predict)]=1

    if Type_template==-1:
        for i in range (0,Exist_predict):
            if Type_types[:,2][i]>=0:
                att[i,int(Type_types[:,2][i]-1)]=1
            if Color_types_predict[i]>=0:
                att[i,int(5+Color_types_predict[i])]=1
            if Size_types_predict[i]>=0:
                att[i,int(15+Size_types_predict[i])]=1
            if Angle_types_predict[i]>=0:
                att[i,int(21+Angle_types_predict[i])]=1

    Place=np.where(Place_predict.reshape(s)==1)[0]
    if Place.size!=Exist_predict:
        Place=np.random.randint(0,s,Exist_predict)

    if Type_template==-1:
        if Place_types_predict[Place_types_predict==1].size==Exist_predict:
            Place=np.zeros(Exist_predict)
            for i in range (0,Exist_predict):
                Place[i]=np.where(Place_types_predict[i,:,:].reshape(s)==1)[0]

    for i in range (0,Exist_predict):
        if max(att[i,0:5])==0:
            att[i,np.random.randint(0,5)]=1
        if max(att[i,5:15])==0:
            att[i,np.random.randint(5,15)]=1
        if max(att[i,15:21])==0:
            att[i,np.random.randint(15,21)]=1
        if max(att[i,21:29])==0:
            att[i,np.random.randint(21,29)]=1

    return att,Place

def pre_draw_simple(Exist_predict,Type_predict,Color_predict,Size_predict,Angle_predict,Type_template,Place_predict,problem_set):
    if problem_set==1 or problem_set==4:
        s=4
    if problem_set==2:
        s=9
    if Exist_predict<=0:
        Exist_predict=np.random.randint(0,s,1)
    Exist_predict=int(Exist_predict)
    att=np.zeros((Exist_predict,29))
    if Type_predict>=0:
        att[:,int(Type_predict-1)]=1
    if Color_predict>=0:
        att[:,int(5+Color_predict)]=1
    if Size_predict>=0:
        att[:,int(15+Size_predict)]=1
    if Angle_predict>=0:
        att[:,int(21+Angle_predict)]=1

    Place=np.where(Place_predict.reshape(s)==1)[0]
    if Place.size!=Exist_predict:
        Place=np.random.randint(0,s,Exist_predict)

    for i in range (0,Exist_predict):
        if max(att[i,0:5])==0:
            att[i,np.random.randint(0,5)]=1
        if max(att[i,5:15])==0:
            att[i,np.random.randint(5,15)]=1
        if max(att[i,15:21])==0:
            att[i,np.random.randint(15,21)]=1
        if max(att[i,21:29])==0:
            att[i,np.random.randint(21,29)]=1

    return att,Place

def pre_draw_centersingle(Type_predict,Color_predict,Size_predict,Angle_predict):
    att=np.zeros(29)
    if Type_predict>=0:
        att[int(Type_predict-1)]=1
    if Color_predict>=0:
        att[int(5+Color_predict)]=1
    if Size_predict>=0:
        att[int(15+Size_predict)]=1
    if Angle_predict>=0:
        att[int(21+Angle_predict)]=1
    if max(att[0:5])==0:
        att[np.random.randint(0,5)]=1
    if max(att[5:15])==0:
        att[np.random.randint(5,15)]=1
    if max(att[15:21])==0:
        att[np.random.randint(15,21)]=1
    if max(att[21:29])==0:
        att[np.random.randint(21,29)]=1
    return att

def pre_draw_outin(Type_predict,Color_predict,Size_predict,Angle_predict,Type_out_predict,Color_out_predict,Size_out_predict,Angle_out_predict):
    att=np.zeros(29)
    if Type_predict>=0:
        att[int(Type_predict-1)]=1
    if Color_predict>=0:
        att[int(5+Color_predict)]=1
    if Size_predict>=0:
        att[int(15+Size_predict)]=1
    if Angle_predict>=0:
        att[int(21+Angle_predict)]=1
    if max(att[0:5])==0:
        att[np.random.randint(0,5)]=1
    if max(att[5:15])==0:
        att[np.random.randint(5,15)]=1
    if max(att[15:21])==0:
        att[np.random.randint(15,21)]=1
    if max(att[21:29])==0:
        att[np.random.randint(21,29)]=1
    
    att_out=np.zeros(29)
    if Type_out_predict>=0:
        att_out[int(Type_out_predict-1)]=1
    if Color_out_predict>=0:
        att_out[int(5+Color_out_predict)]=1
    if Size_out_predict>=0:
        att_out[int(15+Size_out_predict)]=1
    if Angle_out_predict>=0:
        att_out[int(21+Angle_out_predict)]=1
    if max(att_out[0:5])==0:
        att_out[np.random.randint(0,5)]=1
    if max(att_out[5:15])==0:
        att_out[np.random.randint(5,15)]=1
    if max(att_out[15:21])==0:
        att_out[np.random.randint(15,21)]=1
    if max(att_out[21:29])==0:
        att_out[np.random.randint(21,29)]=1
    return att,att_out

def pre_draw_outin4(Exist_predict,Type_predict,Color_predict,Size_predict,Angle_predict,Type_template,Type_types,Color_types_predict,Size_types_predict,Angle_types_predict,Place_predict,Place_types_predict,Type_out_predict,Color_out_predict,Size_out_predict,Angle_out_predict):
    att_out=np.zeros(29)
    if Type_out_predict>=0:
        att_out[int(Type_out_predict-1)]=1
    if Color_out_predict>=0:
        att_out[int(5+Color_out_predict)]=1
    if Size_out_predict>=0:
        att_out[int(15+Size_out_predict)]=1
    if Angle_out_predict>=0:
        att_out[int(21+Angle_out_predict)]=1
    if max(att_out[0:5])==0:
        att_out[np.random.randint(0,5)]=1
    if max(att_out[5:15])==0:
        att_out[np.random.randint(5,15)]=1
    if max(att_out[15:21])==0:
        att_out[np.random.randint(15,21)]=1
    if max(att_out[21:29])==0:
        att_out[np.random.randint(21,29)]=1
    att,Place=pre_draw(Exist_predict,Type_predict,Color_predict,Size_predict,Angle_predict,Type_template,Type_types,Color_types_predict,Size_types_predict,Angle_types_predict,Place_predict,Place_types_predict)
    
    return att,Place,att_out

def pre_draw_outin4_simple(Exist_predict,Type_predict,Color_predict,Size_predict,Angle_predict,Type_template,Place_predict,Type_out_predict,Color_out_predict,Size_out_predict,Angle_out_predict,problem_set):
    att_out=np.zeros(29)
    if Type_out_predict>=0:
        att_out[int(Type_out_predict-1)]=1
    if Color_out_predict>=0:
        att_out[int(5+Color_out_predict)]=1
    if Size_out_predict>=0:
        att_out[int(15+Size_out_predict)]=1
    if Angle_out_predict>=0:
        att_out[int(21+Angle_out_predict)]=1
    if max(att_out[0:5])==0:
        att_out[np.random.randint(0,5)]=1
    if max(att_out[5:15])==0:
        att_out[np.random.randint(5,15)]=1
    if max(att_out[15:21])==0:
        att_out[np.random.randint(15,21)]=1
    if max(att_out[21:29])==0:
        att_out[np.random.randint(21,29)]=1
    att,Place=pre_draw_simple(Exist_predict,Type_predict,Color_predict,Size_predict,Angle_predict,Type_template,Place_predict,problem_set)
    
    return att,Place,att_out
    
    
    