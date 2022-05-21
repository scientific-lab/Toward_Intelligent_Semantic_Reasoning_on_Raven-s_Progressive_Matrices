from torchvision import transforms
import yaml
import torch
import numpy as np
from vae.bvae import BVAE
from collections import OrderedDict
from scipy.ndimage import zoom
from edges import cut_edge
#from vae.models import *

def forward_to_f_2(model_vae,input, **kwargs):
    #print(kwargs['labels'])
    #labels = kwargs['labels']
    mu, log_var = model_vae.encode(input)
    f_1=model_vae.f1(mu)
    f_2=model_vae.f2(f_1)#feature

    #print(self.decode(z).size())
    return  f_2
def generate_Att_from_img(data,t):#twobytwo
    ##load vae models
    with open('vae/bbvae_bvae.yaml', 'r') as file:
        config = yaml.safe_load(file)
    #data = VAEDataset(**config["data_params"], pin_memory=len(config['trainer_params']['gpus']) != 0)
    model_vae = BVAE(**config['model_params'])
    state_dict_vae=torch.load('log_inex/last'+str(t)+'.ckpt',map_location='cpu')
    #state_dict_vae=torch.load('log/bvae/last.ckpt',map_location='cpu')
    state_dict_vae=state_dict_vae['state_dict']

    new_state_dict_vae=OrderedDict()
    for k,v in state_dict_vae.items():
        name=k[6:]
        new_state_dict_vae[name]=v

    model_vae.load_state_dict(new_state_dict_vae)
    model_vae=model_vae.eval()
    Angle=np.ones((2,2,16))*(-1)
    Color=np.ones((2,2,16))*(-1)
    Size=np.ones((2,2,16))*(-1)
    Type=np.ones((2,2,16))*(-1)
    Exist=np.zeros((2,2,16))
    Exist_panel=np.ones(16)*(-1)
    Angle_panel=np.ones(16)*(-1)
    Color_panel=np.ones(16)*(-1)
    Size_panel=np.ones(16)*(-1)
    Type_panel=np.ones(16)*(-1)
    for panel_num in range (0,16):
    #for q in [0]:
        img1=data[panel_num, :80, :80]
        if img1[img1!=255].size!=0:
            img_tensor=transforms.functional.to_tensor(img1)
            f_2=forward_to_f_2(model_vae,img_tensor.reshape(1,1,80,80)).detach().numpy()
            Exist[0,0,panel_num]=1
            Type[0,0,panel_num]=np.argmax(f_2[0][0:5])+1
            Color[0,0,panel_num]=np.argmax(f_2[0][5:15])
            Size[0,0,panel_num]=np.argmax(f_2[0][15:21])
            Angle[0,0,panel_num]=np.argmax(f_2[0][21:29])
        img2=data[panel_num, :80, 80:160]
        if img2[img2!=255].size!=0:
            img_tensor=transforms.functional.to_tensor(img2)
            f_2=forward_to_f_2(model_vae,img_tensor.reshape(1,1,80,80)).detach().numpy()
            Exist[0,1,panel_num]=1
            Type[0,1,panel_num]=np.argmax(f_2[0][0:5])+1
            Color[0,1,panel_num]=np.argmax(f_2[0][5:15])
            Size[0,1,panel_num]=np.argmax(f_2[0][15:21])
            Angle[0,1,panel_num]=np.argmax(f_2[0][21:29])
        img3=data[panel_num, 80:160, :80]
        if img3[img3!=255].size!=0:
            img_tensor=transforms.functional.to_tensor(img3)
            f_2=forward_to_f_2(model_vae,img_tensor.reshape(1,1,80,80)).detach().numpy()
            Exist[1,0,panel_num]=1
            Type[1,0,panel_num]=np.argmax(f_2[0][0:5])+1
            Color[1,0,panel_num]=np.argmax(f_2[0][5:15])
            Size[1,0,panel_num]=np.argmax(f_2[0][15:21])
            Angle[1,0,panel_num]=np.argmax(f_2[0][21:29])
        img4=data[panel_num, 80:160, 80:160]
        if img4[img4!=255].size!=0:
            img_tensor=transforms.functional.to_tensor(img4)
            f_2=forward_to_f_2(model_vae,img_tensor.reshape(1,1,80,80)).detach().numpy()
            Exist[1,1,panel_num]=1
            Type[1,1,panel_num]=np.argmax(f_2[0][0:5])+1
            Color[1,1,panel_num]=np.argmax(f_2[0][5:15])
            Size[1,1,panel_num]=np.argmax(f_2[0][15:21])
            Angle[1,1,panel_num]=np.argmax(f_2[0][21:29])
        Angle[np.where(Type==5)]=0
        Angle[np.where(Type==2)]=Angle[np.where(Type==2)]%2
        Angle[np.where(Type==4)]=Angle[np.where(Type==4)]%4
        Exist_panel[panel_num]=np.sum(Exist[:,:,panel_num])
        #print(Angle[:,:,panel_num][Angle[:,:,panel_num]!=0][0])
        if all(Angle[:,:,panel_num][Angle[:,:,panel_num]!=-1]==Angle[:,:,panel_num][Angle[:,:,panel_num]!=-1][0]):
            Angle_panel[panel_num]=Angle[:,:,panel_num][Angle[:,:,panel_num]!=-1][0]
        if all(Color[:,:,panel_num][Color[:,:,panel_num]!=-1]==Color[:,:,panel_num][Color[:,:,panel_num]!=-1][0]):
            Color_panel[panel_num]=Color[:,:,panel_num][Color[:,:,panel_num]!=-1][0]
        if all(Size[:,:,panel_num][Size[:,:,panel_num]!=-1]==Size[:,:,panel_num][Size[:,:,panel_num]!=-1][0]):
            Size_panel[panel_num]=Size[:,:,panel_num][Size[:,:,panel_num]!=-1][0]
        if all(Type[:,:,panel_num][Type[:,:,panel_num]!=-1]==Type[:,:,panel_num][Type[:,:,panel_num]!=-1][0]):
            Type_panel[panel_num]=Type[:,:,panel_num][Type[:,:,panel_num]!=-1][0]
    return Exist,Type,Color,Size,Angle,Exist_panel,Angle_panel,Color_panel,Size_panel,Type_panel

def generate_Att_from_img_center_single(data):
    ##load vae models
    with open('vae/bbvae_bvae.yaml', 'r') as file:
        config = yaml.safe_load(file)
    #data = VAEDataset(**config["data_params"], pin_memory=len(config['trainer_params']['gpus']) != 0)
    model_vae = BVAE(**config['model_params'])
    state_dict_vae=torch.load('log/bvae/centersingle/last.ckpt',map_location='cpu')
    state_dict_vae=state_dict_vae['state_dict']

    new_state_dict_vae=OrderedDict()
    for k,v in state_dict_vae.items():
        name=k[6:]
        new_state_dict_vae[name]=v

    model_vae.load_state_dict(new_state_dict_vae)
    model_vae=model_vae.eval()
    Angle=np.ones((16))*(-1)
    Color=np.ones((16))*(-1)
    Size=np.ones((16))*(-1)
    Type=np.ones((16))*(-1)
    for panel_num in range (0,16):
        img=data[panel_num,:,:]
        img = zoom(img, (80/160, 80/160))
        img_tensor=transforms.functional.to_tensor(img)
        f_2=forward_to_f_2(model_vae,img_tensor.reshape(1,1,80,80)).detach().numpy()
        Type[panel_num]=np.argmax(f_2[0][0:5])+1
        Color[panel_num]=np.argmax(f_2[0][5:15])
        Size[panel_num]=np.argmax(f_2[0][15:21])
        Angle[panel_num]=np.argmax(f_2[0][21:29])
    Angle[np.where(Type==5)]=0
    Angle[np.where(Type==2)]=Angle[np.where(Type==2)]%2
    Angle[np.where(Type==4)]=Angle[np.where(Type==4)]%4
    return Type,Color,Size,Angle

def generate_Att_from_img_threebythree(data):
    ##load vae models
    with open('vae/bbvae_bvae.yaml', 'r') as file:
        config = yaml.safe_load(file)
    #data = VAEDataset(**config["data_params"], pin_memory=len(config['trainer_params']['gpus']) != 0)
    model_vae = BVAE(**config['model_params'])
    state_dict_vae=torch.load('log/bvae/threebythree/last.ckpt',map_location='cpu')
    state_dict_vae=state_dict_vae['state_dict']

    new_state_dict_vae=OrderedDict()
    for k,v in state_dict_vae.items():
        name=k[6:]
        new_state_dict_vae[name]=v

    model_vae.load_state_dict(new_state_dict_vae)
    model_vae=model_vae.eval()
    
    Angle=np.ones((3,3,16))*(-1)
    Color=np.ones((3,3,16))*(-1)
    Size=np.ones((3,3,16))*(-1)
    Type=np.ones((3,3,16))*(-1)
    Exist=np.zeros((3,3,16))
    Exist_panel=np.ones(16)*(-1)
    Angle_panel=np.ones(16)*(-1)
    Color_panel=np.ones(16)*(-1)
    Size_panel=np.ones(16)*(-1)
    Type_panel=np.ones(16)*(-1)
    for panel_num in range (0,16):
    #for q in [0]:
        img1=data[panel_num, :53, :53]
        if img1[img1!=255].size!=0:
            img1 = zoom(img1, (80/53, 80/53))
            img_tensor=transforms.functional.to_tensor(img1)
            f_2=forward_to_f_2(model_vae,img_tensor.reshape(1,1,80,80)).detach().numpy()
            Exist[0,0,panel_num]=1
            Type[0,0,panel_num]=np.argmax(f_2[0][0:5])+1
            Color[0,0,panel_num]=np.argmax(f_2[0][5:15])
            Size[0,0,panel_num]=np.argmax(f_2[0][15:21])
            Angle[0,0,panel_num]=np.argmax(f_2[0][21:29])
        img2=data[panel_num, :53, 54:107]
        if img2[img2!=255].size!=0:
            img2 = zoom(img2, (80/53, 80/53))
            img_tensor=transforms.functional.to_tensor(img2)
            f_2=forward_to_f_2(model_vae,img_tensor.reshape(1,1,80,80)).detach().numpy()
            Exist[0,1,panel_num]=1
            Type[0,1,panel_num]=np.argmax(f_2[0][0:5])+1
            Color[0,1,panel_num]=np.argmax(f_2[0][5:15])
            Size[0,1,panel_num]=np.argmax(f_2[0][15:21])
            Angle[0,1,panel_num]=np.argmax(f_2[0][21:29])
        img3=data[panel_num, :53, 107:160]
        if img3[img3!=255].size!=0:
            img3 = zoom(img3, (80/53, 80/53))
            img_tensor=transforms.functional.to_tensor(img3)
            f_2=forward_to_f_2(model_vae,img_tensor.reshape(1,1,80,80)).detach().numpy()
            Exist[0,2,panel_num]=1
            Type[0,2,panel_num]=np.argmax(f_2[0][0:5])+1
            Color[0,2,panel_num]=np.argmax(f_2[0][5:15])
            Size[0,2,panel_num]=np.argmax(f_2[0][15:21])
            Angle[0,2,panel_num]=np.argmax(f_2[0][21:29])
        img4=data[panel_num, 54:107, :53]
        if img4[img4!=255].size!=0:
            img4 = zoom(img4, (80/53, 80/53))
            img_tensor=transforms.functional.to_tensor(img4)
            f_2=forward_to_f_2(model_vae,img_tensor.reshape(1,1,80,80)).detach().numpy()
            Exist[1,0,panel_num]=1
            Type[1,0,panel_num]=np.argmax(f_2[0][0:5])+1
            Color[1,0,panel_num]=np.argmax(f_2[0][5:15])
            Size[1,0,panel_num]=np.argmax(f_2[0][15:21])
            Angle[1,0,panel_num]=np.argmax(f_2[0][21:29])
        img5=data[panel_num, 54:107, 54:107]
        if img5[img5!=255].size!=0:
            img5 = zoom(img5, (80/53, 80/53))
            img_tensor=transforms.functional.to_tensor(img5)
            f_2=forward_to_f_2(model_vae,img_tensor.reshape(1,1,80,80)).detach().numpy()
            Exist[1,1,panel_num]=1
            Type[1,1,panel_num]=np.argmax(f_2[0][0:5])+1
            Color[1,1,panel_num]=np.argmax(f_2[0][5:15])
            Size[1,1,panel_num]=np.argmax(f_2[0][15:21])
            Angle[1,1,panel_num]=np.argmax(f_2[0][21:29])
        img6=data[panel_num, 54:107, 107:160]
        if img6[img6!=255].size!=0:
            img6 = zoom(img6, (80/53, 80/53))
            img_tensor=transforms.functional.to_tensor(img6)
            f_2=forward_to_f_2(model_vae,img_tensor.reshape(1,1,80,80)).detach().numpy()
            Exist[1,2,panel_num]=1
            Type[1,2,panel_num]=np.argmax(f_2[0][0:5])+1
            Color[1,2,panel_num]=np.argmax(f_2[0][5:15])
            Size[1,2,panel_num]=np.argmax(f_2[0][15:21])
            Angle[1,2,panel_num]=np.argmax(f_2[0][21:29])
        img7=data[panel_num, 107:160, :53]
        if img7[img7!=255].size!=0:
            img7 = zoom(img7, (80/53, 80/53))
            img_tensor=transforms.functional.to_tensor(img7)
            f_2=forward_to_f_2(model_vae,img_tensor.reshape(1,1,80,80)).detach().numpy()
            Exist[2,0,panel_num]=1
            Type[2,0,panel_num]=np.argmax(f_2[0][0:5])+1
            Color[2,0,panel_num]=np.argmax(f_2[0][5:15])
            Size[2,0,panel_num]=np.argmax(f_2[0][15:21])
            Angle[2,0,panel_num]=np.argmax(f_2[0][21:29])
        img8=data[panel_num, 107:160, 54:107]
        if img8[img8!=255].size!=0:
            img8 = zoom(img8, (80/53, 80/53))
            img_tensor=transforms.functional.to_tensor(img8)
            f_2=forward_to_f_2(model_vae,img_tensor.reshape(1,1,80,80)).detach().numpy()
            Exist[2,1,panel_num]=1
            Type[2,1,panel_num]=np.argmax(f_2[0][0:5])+1
            Color[2,1,panel_num]=np.argmax(f_2[0][5:15])
            Size[2,1,panel_num]=np.argmax(f_2[0][15:21])
            Angle[2,1,panel_num]=np.argmax(f_2[0][21:29])
        img9=data[panel_num, 107:160, 107:160]
        if img9[img9!=255].size!=0:
            img9 = zoom(img9, (80/53, 80/53))
            img_tensor=transforms.functional.to_tensor(img9)
            f_2=forward_to_f_2(model_vae,img_tensor.reshape(1,1,80,80)).detach().numpy()
            Exist[2,2,panel_num]=1
            Type[2,2,panel_num]=np.argmax(f_2[0][0:5])+1
            Color[2,2,panel_num]=np.argmax(f_2[0][5:15])
            Size[2,2,panel_num]=np.argmax(f_2[0][15:21])
            Angle[2,2,panel_num]=np.argmax(f_2[0][21:29])
        Angle[np.where(Type==5)]=0
        Angle[np.where(Type==2)]=Angle[np.where(Type==2)]%2
        Angle[np.where(Type==4)]=Angle[np.where(Type==4)]%4
        Exist_panel[panel_num]=np.sum(Exist[:,:,panel_num])
        if all(Angle[:,:,panel_num][Angle[:,:,panel_num]!=-1]==Angle[:,:,panel_num][Angle[:,:,panel_num]!=-1][0]):
            Angle_panel[panel_num]=Angle[:,:,panel_num][Angle[:,:,panel_num]!=-1][0]
        if all(Color[:,:,panel_num][Color[:,:,panel_num]!=-1]==Color[:,:,panel_num][Color[:,:,panel_num]!=-1][0]):
            Color_panel[panel_num]=Color[:,:,panel_num][Color[:,:,panel_num]!=-1][0]
        if all(Size[:,:,panel_num][Size[:,:,panel_num]!=-1]==Size[:,:,panel_num][Size[:,:,panel_num]!=-1][0]):
            Size_panel[panel_num]=Size[:,:,panel_num][Size[:,:,panel_num]!=-1][0]
        if all(Type[:,:,panel_num][Type[:,:,panel_num]!=-1]==Type[:,:,panel_num][Type[:,:,panel_num]!=-1][0]):
            Type_panel[panel_num]=Type[:,:,panel_num][Type[:,:,panel_num]!=-1][0]
    return Exist,Type,Color,Size,Angle,Exist_panel,Angle_panel,Color_panel,Size_panel,Type_panel

def generate_Att_from_img_in_out_single(data):
    ##load vae models
    with open('vae/bbvae_bvae.yaml', 'r') as file:
        config = yaml.safe_load(file)
    #data = VAEDataset(**config["data_params"], pin_memory=len(config['trainer_params']['gpus']) != 0)
    model_vae = BVAE(**config['model_params'])
    state_dict_vae=torch.load('log/bvae/in_center_single_out_center_single/in/last.ckpt',map_location='cpu')
    state_dict_vae=state_dict_vae['state_dict']

    new_state_dict_vae=OrderedDict()
    for k,v in state_dict_vae.items():
        name=k[6:]
        new_state_dict_vae[name]=v

    model_vae.load_state_dict(new_state_dict_vae)
    model_vae=model_vae.eval()
    
    with open('vae/bbvae_bvae.yaml', 'r') as file:
        config = yaml.safe_load(file)
    #data = VAEDataset(**config["data_params"], pin_memory=len(config['trainer_params']['gpus']) != 0)
    model_vae1 = BVAE(**config['model_params'])
    state_dict_vae1=torch.load('log/bvae/in_center_single_out_center_single/out/last.ckpt',map_location='cpu')
    state_dict_vae1=state_dict_vae1['state_dict']

    new_state_dict_vae1=OrderedDict()
    for k,v in state_dict_vae1.items():
        name=k[6:]
        new_state_dict_vae1[name]=v

    model_vae1.load_state_dict(new_state_dict_vae1)
    model_vae1=model_vae1.eval()
    
    Angle=np.ones((16))*(-1)
    Color=np.ones((16))*(-1)
    Size=np.ones((16))*(-1)
    Type=np.ones((16))*(-1)
    
    Angle_out=np.ones((16))*(-1)
    Color_out=np.ones((16))*(-1)
    Size_out=np.ones((16))*(-1)
    Type_out=np.ones((16))*(-1)
    ind=np.load('ind.npy')
    for panel_num in range (0,16):
        img=data[panel_num,54:107, 54:107]
        img[ind==1]=255
        img = zoom(img, (80/53, 80/53))
        img_tensor=transforms.functional.to_tensor(img)
        f_2=forward_to_f_2(model_vae,img_tensor.reshape(1,1,80,80)).detach().numpy()
        Type[panel_num]=np.argmax(f_2[0][0:5])+1
        Color[panel_num]=np.argmax(f_2[0][5:15])
        Size[panel_num]=np.argmax(f_2[0][15:21])
        Angle[panel_num]=np.argmax(f_2[0][21:29])
    Angle[np.where(Type==5)]=0
    Angle[np.where(Type==2)]=Angle[np.where(Type==2)]%2
    Angle[np.where(Type==4)]=Angle[np.where(Type==4)]%4
    
    for panel_num in range (0,16):
        img=data[panel_num,:, :]
        img[54:107, 54:107][ind==0]=255
        img = zoom(img, (80/160, 80/160))
        img_tensor=transforms.functional.to_tensor(img)
        f_2=forward_to_f_2(model_vae1,img_tensor.reshape(1,1,80,80)).detach().numpy()
        Type_out[panel_num]=np.argmax(f_2[0][0:5])+1
        Color_out[panel_num]=np.argmax(f_2[0][5:15])
        Size_out[panel_num]=np.argmax(f_2[0][15:21])
        Angle_out[panel_num]=np.argmax(f_2[0][21:29])
    Angle_out[np.where(Type_out==5)]=0
    Angle_out[np.where(Type_out==2)]=Angle_out[np.where(Type_out==2)]%2
    Angle_out[np.where(Type_out==4)]=Angle_out[np.where(Type_out==4)]%4
    return Type,Color,Size,Angle,Type_out,Color_out,Size_out,Angle_out

def generate_Att_from_img_outin4(data):#twobytwo
    ##load vae models
    with open('vae/bbvae_bvae.yaml', 'r') as file:
        config = yaml.safe_load(file)
    #data = VAEDataset(**config["data_params"], pin_memory=len(config['trainer_params']['gpus']) != 0)
    model_vae = BVAE(**config['model_params'])
    state_dict_vae=torch.load('log/bvae/in_distribute_four_out_center_single/in/last.ckpt',map_location='cpu')
    state_dict_vae=state_dict_vae['state_dict']

    new_state_dict_vae=OrderedDict()
    for k,v in state_dict_vae.items():
        name=k[6:]
        new_state_dict_vae[name]=v

    model_vae.load_state_dict(new_state_dict_vae)
    model_vae=model_vae.eval()
    
    with open('vae/bbvae_bvae.yaml', 'r') as file:
        config = yaml.safe_load(file)
    #data = VAEDataset(**config["data_params"], pin_memory=len(config['trainer_params']['gpus']) != 0)
    model_vae1 = BVAE(**config['model_params'])
    state_dict_vae1=torch.load('log/bvae/in_distribute_four_out_center_single/out/last.ckpt',map_location='cpu')
    state_dict_vae1=state_dict_vae1['state_dict']

    new_state_dict_vae1=OrderedDict()
    for k,v in state_dict_vae1.items():
        name=k[6:]
        new_state_dict_vae1[name]=v

    model_vae1.load_state_dict(new_state_dict_vae1)
    model_vae1=model_vae1.eval()
    
    Angle=np.ones((2,2,16))*(-1)
    Color=np.ones((2,2,16))*(-1)
    Size=np.ones((2,2,16))*(-1)
    Type=np.ones((2,2,16))*(-1)
    Exist=np.zeros((2,2,16))
    Exist_panel=np.ones(16)*(-1)
    Angle_panel=np.ones(16)*(-1)
    Color_panel=np.ones(16)*(-1)
    Size_panel=np.ones(16)*(-1)
    Type_panel=np.ones(16)*(-1)
    
    Angle_out=np.ones((16))*(-1)
    Color_out=np.ones((16))*(-1)
    Size_out=np.ones((16))*(-1)
    Type_out=np.ones((16))*(-1)
    
    for panel_num in range (0,16):
    #for q in [0]:
        img1=data[panel_num, 55:79, 55:79]
        img1,area1=cut_edge(img1)
        if img1[img1!=255].size>20:
            img1 = zoom(img1, (80/24, 80/24),order=0)
            img_tensor=transforms.functional.to_tensor(img1)
            f_2=forward_to_f_2(model_vae,img_tensor.reshape(1,1,80,80)).detach().numpy()
            Exist[0,0,panel_num]=1
            Type[0,0,panel_num]=np.argmax(f_2[0][0:5])+1
            Color[0,0,panel_num]=np.argmax(f_2[0][5:15])
            Size[0,0,panel_num]=np.argmax(f_2[0][15:21])
            Angle[0,0,panel_num]=np.argmax(f_2[0][21:29])
        img2=data[panel_num, 55:79, 81:105]
        img2,area2=cut_edge(img2)
        if img2[img2!=255].size>20:
            img2 = zoom(img2, (80/24, 80/24),order=0)
            img_tensor=transforms.functional.to_tensor(img2)
            f_2=forward_to_f_2(model_vae,img_tensor.reshape(1,1,80,80)).detach().numpy()
            Exist[0,1,panel_num]=1
            Type[0,1,panel_num]=np.argmax(f_2[0][0:5])+1
            Color[0,1,panel_num]=np.argmax(f_2[0][5:15])
            Size[0,1,panel_num]=np.argmax(f_2[0][15:21])
            Angle[0,1,panel_num]=np.argmax(f_2[0][21:29])
        img3=data[panel_num, 81:105, 55:79]
        img3,area3=cut_edge(img3)
        if img3[img3!=255].size>20:
            img3 = zoom(img3, (80/24, 80/24),order=0)
            img_tensor=transforms.functional.to_tensor(img3)
            f_2=forward_to_f_2(model_vae,img_tensor.reshape(1,1,80,80)).detach().numpy()
            Exist[1,0,panel_num]=1
            Type[1,0,panel_num]=np.argmax(f_2[0][0:5])+1
            Color[1,0,panel_num]=np.argmax(f_2[0][5:15])
            Size[1,0,panel_num]=np.argmax(f_2[0][15:21])
            Angle[1,0,panel_num]=np.argmax(f_2[0][21:29])
        img4=data[panel_num, 81:105, 81:105]
        img4,area4=cut_edge(img4)
        if img4[img4!=255].size>20:
            img4 = zoom(img4, (80/24, 80/24),order=0)
            img_tensor=transforms.functional.to_tensor(img4)
            f_2=forward_to_f_2(model_vae,img_tensor.reshape(1,1,80,80)).detach().numpy()
            Exist[1,1,panel_num]=1
            Type[1,1,panel_num]=np.argmax(f_2[0][0:5])+1
            Color[1,1,panel_num]=np.argmax(f_2[0][5:15])
            Size[1,1,panel_num]=np.argmax(f_2[0][15:21])
            Angle[1,1,panel_num]=np.argmax(f_2[0][21:29])
        Angle[np.where(Type==5)]=0
        Angle[np.where(Type==2)]=Angle[np.where(Type==2)]%2
        Angle[np.where(Type==4)]=Angle[np.where(Type==4)]%4
        Exist_panel[panel_num]=np.sum(Exist[:,:,panel_num])
        #print(Angle[:,:,panel_num][Angle[:,:,panel_num]!=-1][0])
        if Angle[:,:,panel_num][Angle[:,:,panel_num]!=-1].size>0:
            if all(Angle[:,:,panel_num][Angle[:,:,panel_num]!=-1]==Angle[:,:,panel_num][Angle[:,:,panel_num]!=-1][0]):
                Angle_panel[panel_num]=Angle[:,:,panel_num][Angle[:,:,panel_num]!=-1][0]
            if all(Color[:,:,panel_num][Color[:,:,panel_num]!=-1]==Color[:,:,panel_num][Color[:,:,panel_num]!=-1][0]):
                Color_panel[panel_num]=Color[:,:,panel_num][Color[:,:,panel_num]!=-1][0]
            if all(Size[:,:,panel_num][Size[:,:,panel_num]!=-1]==Size[:,:,panel_num][Size[:,:,panel_num]!=-1][0]):
                Size_panel[panel_num]=Size[:,:,panel_num][Size[:,:,panel_num]!=-1][0]
            if all(Type[:,:,panel_num][Type[:,:,panel_num]!=-1]==Type[:,:,panel_num][Type[:,:,panel_num]!=-1][0]):
                Type_panel[panel_num]=Type[:,:,panel_num][Type[:,:,panel_num]!=-1][0]
        
        img=data[panel_num,:, :]           
        img[55:79, 55:79][area1==0]=255
        img[55:79, 81:105][area2==0]=255
        img[81:105, 55:79][area3==0]=255
        img[81:105, 81:105][area4==0]=255
        
        img = zoom(img, (80/160, 80/160))
        img_tensor=transforms.functional.to_tensor(img)
        f_2=forward_to_f_2(model_vae1,img_tensor.reshape(1,1,80,80)).detach().numpy()
        Type_out[panel_num]=np.argmax(f_2[0][0:5])+1
        Color_out[panel_num]=np.argmax(f_2[0][5:15])
        Size_out[panel_num]=np.argmax(f_2[0][15:21])
        Angle_out[panel_num]=np.argmax(f_2[0][21:29])
    return Exist,Type,Color,Size,Angle,Exist_panel,Angle_panel,Color_panel,Size_panel,Type_panel,Type_out,Color_out,Size_out,Angle_out

def generate_Att_from_img_leftright(data):
    ##load vae models
    with open('vae/bbvae_bvae.yaml', 'r') as file:
        config = yaml.safe_load(file)
    #data = VAEDataset(**config["data_params"], pin_memory=len(config['trainer_params']['gpus']) != 0)
    model_vae = BVAE(**config['model_params'])
    state_dict_vae=torch.load('log/bvae/leftright/last.ckpt',map_location='cpu')
    state_dict_vae=state_dict_vae['state_dict']

    new_state_dict_vae=OrderedDict()
    for k,v in state_dict_vae.items():
        name=k[6:]
        new_state_dict_vae[name]=v

    model_vae.load_state_dict(new_state_dict_vae)
    model_vae=model_vae.eval()
    
    Angle_1=np.ones((16))*(-1)
    Color_1=np.ones((16))*(-1)
    Size_1=np.ones((16))*(-1)
    Type_1=np.ones((16))*(-1)
    
    Angle_2=np.ones((16))*(-1)
    Color_2=np.ones((16))*(-1)
    Size_2=np.ones((16))*(-1)
    Type_2=np.ones((16))*(-1)
    for panel_num in range (0,16):
        img=data[panel_num,40:120, :80]
        #img = zoom(img, (80/53, 80/53))
        img_tensor=transforms.functional.to_tensor(img)
        f_2=forward_to_f_2(model_vae,img_tensor.reshape(1,1,80,80)).detach().numpy()
        Type_1[panel_num]=np.argmax(f_2[0][0:5])+1
        Color_1[panel_num]=np.argmax(f_2[0][5:15])
        Size_1[panel_num]=np.argmax(f_2[0][15:21])
        Angle_1[panel_num]=np.argmax(f_2[0][21:29])
    Angle_1[np.where(Type_1==5)]=0
    Angle_1[np.where(Type_1==2)]=Angle_1[np.where(Type_1==2)]%2
    Angle_1[np.where(Type_1==4)]=Angle_1[np.where(Type_1==4)]%4
    
    for panel_num in range (0,16):
        img=data[panel_num,40:120, 80:160]
        #img = zoom(img, (80/160, 80/160))
        img_tensor=transforms.functional.to_tensor(img)
        f_2=forward_to_f_2(model_vae,img_tensor.reshape(1,1,80,80)).detach().numpy()
        Type_2[panel_num]=np.argmax(f_2[0][0:5])+1
        Color_2[panel_num]=np.argmax(f_2[0][5:15])
        Size_2[panel_num]=np.argmax(f_2[0][15:21])
        Angle_2[panel_num]=np.argmax(f_2[0][21:29])
    Angle_2[np.where(Type_2==5)]=0
    Angle_2[np.where(Type_2==2)]=Angle_2[np.where(Type_2==2)]%2
    Angle_2[np.where(Type_2==4)]=Angle_2[np.where(Type_2==4)]%4
    return Type_1,Color_1,Size_1,Angle_1,Type_2,Color_2,Size_2,Angle_2

def generate_Att_from_img_updown(data):
    ##load vae models
    with open('vae/bbvae_bvae.yaml', 'r') as file:
        config = yaml.safe_load(file)
    #data = VAEDataset(**config["data_params"], pin_memory=len(config['trainer_params']['gpus']) != 0)
    model_vae = BVAE(**config['model_params'])
    state_dict_vae=torch.load('log/bvae/updown/last.ckpt',map_location='cpu')
    state_dict_vae=state_dict_vae['state_dict']

    new_state_dict_vae=OrderedDict()
    for k,v in state_dict_vae.items():
        name=k[6:]
        new_state_dict_vae[name]=v

    model_vae.load_state_dict(new_state_dict_vae)
    model_vae=model_vae.eval()
    
    Angle_1=np.ones((16))*(-1)
    Color_1=np.ones((16))*(-1)
    Size_1=np.ones((16))*(-1)
    Type_1=np.ones((16))*(-1)
    
    Angle_2=np.ones((16))*(-1)
    Color_2=np.ones((16))*(-1)
    Size_2=np.ones((16))*(-1)
    Type_2=np.ones((16))*(-1)
    for panel_num in range (0,16):
        img=data[panel_num,:80,40:120]
        #img = zoom(img, (80/53, 80/53))
        img_tensor=transforms.functional.to_tensor(img)
        f_2=forward_to_f_2(model_vae,img_tensor.reshape(1,1,80,80)).detach().numpy()
        Type_1[panel_num]=np.argmax(f_2[0][0:5])+1
        Color_1[panel_num]=np.argmax(f_2[0][5:15])
        Size_1[panel_num]=np.argmax(f_2[0][15:21])
        Angle_1[panel_num]=np.argmax(f_2[0][21:29])
    Angle_1[np.where(Type_1==5)]=0
    Angle_1[np.where(Type_1==2)]=Angle_1[np.where(Type_1==2)]%2
    Angle_1[np.where(Type_1==4)]=Angle_1[np.where(Type_1==4)]%4
    
    for panel_num in range (0,16):
        img=data[panel_num,80:160,40:120]
        #img = zoom(img, (80/160, 80/160))
        img_tensor=transforms.functional.to_tensor(img)
        f_2=forward_to_f_2(model_vae,img_tensor.reshape(1,1,80,80)).detach().numpy()
        Type_2[panel_num]=np.argmax(f_2[0][0:5])+1
        Color_2[panel_num]=np.argmax(f_2[0][5:15])
        Size_2[panel_num]=np.argmax(f_2[0][15:21])
        Angle_2[panel_num]=np.argmax(f_2[0][21:29])
    Angle_2[np.where(Type_2==5)]=0
    Angle_2[np.where(Type_2==2)]=Angle_2[np.where(Type_2==2)]%2
    Angle_2[np.where(Type_2==4)]=Angle_2[np.where(Type_2==4)]%4
    return Type_1,Color_1,Size_1,Angle_1,Type_2,Color_2,Size_2,Angle_2