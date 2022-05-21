import numpy as np
def check_panel_sort(Att,Candidate):
    s=Att[:,:,0].size
    if (np.sort(Att[:,:,0].reshape(s))==np.sort(Att[:,:,1].reshape(s))).all() and (np.sort(Att[:,:,1].reshape(s))==np.sort(Att[:,:,2].reshape(s))).all():
        if (np.sort(Att[:,:,3].reshape(s))==np.sort(Att[:,:,4].reshape(s))).all() and (np.sort(Att[:,:,4].reshape(s))==np.sort(Att[:,:,5].reshape(s))).all():
            if (np.sort(Att[:,:,6].reshape(s))==np.sort(Att[:,:,7].reshape(s))).all():
                for i in range (8,16):
                    if (np.sort(Att[:,:,i].reshape(s))!=np.sort(Att[:,:,7].reshape(s))).any():
                        Candidate[i-8]-=1
    return Candidate

def check_panel_predict(predict,panel,Candidate):
    if predict!=-1:
        Candidate[panel[8:16]==-1]-=1
        if predict!=-2:
            Candidate[panel[8:16]!=predict]-=1
    return Candidate

def check_place_predict(Place_template,Exist,Place_predict,Candidate):
    if Place_template!=-1:
        c=np.ones(8)
        for w in range (8,16):
            E=Exist[:,:,w]
            if (E!=Place_predict).any():
                c[w-8]=0
        #print(c)
        Candidate[c==0]-=1
    return Candidate

def check_types_match(predict,types,Candidate):
    if predict[predict>0].size>0:
        for i in range (8,16):
            if (predict!=types[:,i]).any():
                Candidate[i-8]-=1
    return Candidate

def check_types_place(Place_types_predict,Place_types,Candidate):
    if Place_types_predict[Place_types_predict>0].size>0:
        for i in range (8,16):
            if (Place_types_predict!=Place_types[:,i,:,:]).any():
                Candidate[i-8]-=1
    return Candidate