import os
import numpy as np
from generate_att import generate_Att_from_img_center_single
from reasoning.general_template_panel_and_ind import general_template
Name=os.listdir('D:\\zsk\\SRAN-master\\I-RAVEN-test\\center_single')
k=0
for name_ind in range (0,5000):
        #for name_ind in [0,1]:
    length=len('RAVEN_'+str(name_ind)+'_')
    for n in Name:
        if n[0:length]=='RAVEN_'+str(name_ind)+'_' and n[-3:]=='npz':
            Type0=np.zeros(9)
            Size0=np.zeros(9)
            Color0=np.zeros(9)
            #A=np.load('D:\\zsk\\RAVEN\\I-RAVEN\\center_single\\'+n)
            A=np.load('D:\\zsk\\SRAN-master\\I-RAVEN-test\\center_single\\'+n)
            data=A['image']
            answer=A['target']
            Type,Color,Size,Angle=generate_Att_from_img_center_single(data)
            Type0[0:8]=Type[0:8]
            Type0[8]=Type[answer+8]
            Color0[0:8]=Color[0:8]
            Color0[8]=Color[answer+8]
            Size0[0:8]=Size[0:8]
            Size0[8]=Size[answer+8]
            Type_c=Type[8:16]
            Color_c=Color[8:16]
            Size_c=Size[8:16]
            np.save('D:\\zsk\\RAVEN\\data_9_test\\'+str(k)+'.npy',Type0)
            np.save('D:\\zsk\\RAVEN\\select8_test\\'+str(k)+'.npy',Type_c)
            k+=1
            np.save('D:\\zsk\\RAVEN\\data_9_test\\'+str(k)+'.npy',Color0)
            np.save('D:\\zsk\\RAVEN\\select8_test\\'+str(k)+'.npy',Color_c)
            k+=1
            np.save('D:\\zsk\\RAVEN\\data_9_test\\'+str(k)+'.npy',Size0)
            np.save('D:\\zsk\\RAVEN\\select8_test\\'+str(k)+'.npy',Size_c)
            k+=1

            