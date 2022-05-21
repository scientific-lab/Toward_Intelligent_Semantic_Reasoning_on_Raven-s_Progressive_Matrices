from torchvision import transforms
import yaml
import torch
import numpy as np
from vae.bvae import BVAE
from collections import OrderedDict
from scipy.ndimage import zoom
#from vae.models import *


def forward_f_2(model_vae,f_2):
        #print(kwargs['labels'])
        #labels = kwargs['labels']
        f_3=model_vae.f3(f_2)
        f_4=model_vae.f4(f_3)
        #z2 = model.reparameterize(f_4, log_var)
        
        #print(self.decode(z).size())
        return  model_vae.decode(f_4)
def draw_pic(att,Place):
    ##load vae models
    with open('vae/bbvae_bvae.yaml', 'r') as file:
        config = yaml.safe_load(file)
    #data = VAEDataset(**config["data_params"], pin_memory=len(config['trainer_params']['gpus']) != 0)
    model_vae = BVAE(**config['model_params'])

    state_dict_vae=torch.load('log\\bvae\\last.ckpt', map_location='cpu')
    state_dict_vae=state_dict_vae['state_dict']

    new_state_dict_vae=OrderedDict()
    for k,v in state_dict_vae.items():
        name=k[6:]
        new_state_dict_vae[name]=v

    model_vae.load_state_dict(new_state_dict_vae)
    model_vae=model_vae.eval()
    img_whole=np.zeros((160,160))   
    for i in range (0,att.shape[0]):
        f_2_tensor=torch.from_numpy(att[i]).float()
        img=forward_f_2(model_vae,f_2_tensor).detach().numpy()[0,0,:,:]
        if Place[i]==0:
            img_whole[:80, :80]=img
        if Place[i]==1:
            img_whole[:80, 80:160]=img
        if Place[i]==2:
            img_whole[80:160, :80]=img
        if Place[i]==3:
            img_whole[80:160, 80:160]=img

    if Place[Place==0].size==0:
        img_whole[:80, :80]=1
    if Place[Place==1].size==0:
        img_whole[:80, 80:160]=1
    if Place[Place==2].size==0:
        img_whole[80:160, :80]=1
    if Place[Place==3].size==0:
        img_whole[80:160, 80:160]=1
    return img_whole

def draw_pic_centersingle(att):
    ##load vae models
    with open('vae/bbvae_bvae.yaml', 'r') as file:
        config = yaml.safe_load(file)
    #data = VAEDataset(**config["data_params"], pin_memory=len(config['trainer_params']['gpus']) != 0)
    model_vae = BVAE(**config['model_params'])
    state_dict_vae=torch.load('log\\bvae\\centersingle\\last.ckpt', map_location='cpu')
    state_dict_vae=state_dict_vae['state_dict']

    new_state_dict_vae=OrderedDict()
    for k,v in state_dict_vae.items():
        name=k[6:]
        new_state_dict_vae[name]=v

    model_vae.load_state_dict(new_state_dict_vae)
    model_vae=model_vae.eval()
    f_2_tensor=torch.from_numpy(att).float()
    img=forward_f_2(model_vae,f_2_tensor).detach().numpy()[0,0,:,:]
    img = zoom(img, (160/80, 160/80))
    return img

def draw_pic_threebythree(att,Place):
    ##load vae models
    with open('vae/bbvae_bvae.yaml', 'r') as file:
        config = yaml.safe_load(file)
    #data = VAEDataset(**config["data_params"], pin_memory=len(config['trainer_params']['gpus']) != 0)
    model_vae = BVAE(**config['model_params'])

    state_dict_vae=torch.load('log\\bvae\\threebythree\\last.ckpt', map_location='cpu')
    state_dict_vae=state_dict_vae['state_dict']

    new_state_dict_vae=OrderedDict()
    for k,v in state_dict_vae.items():
        name=k[6:]
        new_state_dict_vae[name]=v

    model_vae.load_state_dict(new_state_dict_vae)
    model_vae=model_vae.eval()
    img_whole=np.zeros((160,160))   
    for i in range (0,att.shape[0]):
        f_2_tensor=torch.from_numpy(att[i]).float()
        img=forward_f_2(model_vae,f_2_tensor).detach().numpy()[0,0,:,:]
        img = zoom(img, (53/80, 53/80))
        if Place[i]==0:
            img_whole[:53, :53]=img
        if Place[i]==1:
            img_whole[:53, 54:107]=img
        if Place[i]==2:
            img_whole[:53, 107:160]=img
        if Place[i]==3:
            img_whole[54:107, :53]=img
        if Place[i]==4:
            img_whole[54:107, 54:107]=img
        if Place[i]==5:
            img_whole[54:107, 107:160]=img
        if Place[i]==6:
            img_whole[107:160, :53]=img
        if Place[i]==7:
            img_whole[107:160, 54:107]=img
        if Place[i]==8:
            img_whole[107:160, 107:160]=img

    if Place[Place==0].size==0:
        img_whole[:53, :53]=1
    if Place[Place==1].size==0:
        img_whole[:53, 54:107]=1
    if Place[Place==2].size==0:
        img_whole[:53, 107:160]=1
    if Place[Place==3].size==0:
        img_whole[54:107, :53]=1
    if Place[Place==4].size==0:
        img_whole[54:107, 54:107]=1
    if Place[Place==5].size==0:
        img_whole[54:107, 107:160]=1
    if Place[Place==6].size==0:
        img_whole[107:160, :53]=1
    if Place[Place==7].size==0:
        img_whole[107:160, 54:107]=1
    if Place[Place==8].size==0:
        img_whole[107:160, 107:160]=1
    img_whole[53,:]=1
    img_whole[:,53]=1
    return img_whole

def draw_pic_outin(att,att_out):
    ##load vae models
    with open('vae/bbvae_bvae.yaml', 'r') as file:
        config = yaml.safe_load(file)
    #data = VAEDataset(**config["data_params"], pin_memory=len(config['trainer_params']['gpus']) != 0)
    model_vae = BVAE(**config['model_params'])
    state_dict_vae=torch.load('log\\bvae\\in_center_single_out_center_single\\in\\last.ckpt', map_location='cpu')
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
    state_dict_vae1=torch.load('log\\bvae\\in_center_single_out_center_single\\out\\last.ckpt', map_location='cpu')
    state_dict_vae1=state_dict_vae1['state_dict']

    new_state_dict_vae1=OrderedDict()
    for k,v in state_dict_vae1.items():
        name=k[6:]
        new_state_dict_vae1[name]=v

    model_vae1.load_state_dict(new_state_dict_vae1)
    model_vae1=model_vae1.eval()
    
    
    f_2_tensor=torch.from_numpy(att_out).float()
    img=forward_f_2(model_vae1,f_2_tensor).detach().numpy()[0,0,:,:]
    img = zoom(img, (160/80, 160/80))
    
    f_2_tensor1=torch.from_numpy(att).float()
    img1=forward_f_2(model_vae,f_2_tensor1).detach().numpy()[0,0,:,:]
    img1 = zoom(img1, (53/80, 53/80))
    ind=np.load('ind.npy')
    img[54:107,54:107][ind==0]=img1[ind==0]
    return img

def draw_pic_outin4(att,Place,att_out):
    with open('vae/bbvae_bvae.yaml', 'r') as file:
        config = yaml.safe_load(file)
    #data = VAEDataset(**config["data_params"], pin_memory=len(config['trainer_params']['gpus']) != 0)
    model_vae = BVAE(**config['model_params'])
    state_dict_vae=torch.load('log\\bvae\\in_distribute_four_out_center_single\\in\\last.ckpt', map_location='cpu')
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
    state_dict_vae1=torch.load('log\\bvae\\in_distribute_four_out_center_single\\out\\last.ckpt', map_location='cpu')
    state_dict_vae1=state_dict_vae1['state_dict']

    new_state_dict_vae1=OrderedDict()
    for k,v in state_dict_vae1.items():
        name=k[6:]
        new_state_dict_vae1[name]=v

    model_vae1.load_state_dict(new_state_dict_vae1)
    model_vae1=model_vae1.eval()
    
    img_whole=np.ones((160,160))   
    for i in range (0,att.shape[0]):
        f_2_tensor=torch.from_numpy(att[i]).float()
        img=forward_f_2(model_vae,f_2_tensor).detach().numpy()[0,0,:,:]
        img = zoom(img, (24/80, 24/80))
        if Place[i]==0:
            img_whole[55:79, 55:79]=img
        if Place[i]==1:
            img_whole[55:79, 81:105]=img
        if Place[i]==2:
            img_whole[81:105, 55:79]=img
        if Place[i]==3:
            img_whole[81:105, 81:105]=img

    if Place[Place==0].size==0:
        img_whole[55:79, 55:79]=1
    if Place[Place==1].size==0:
        img_whole[55:79, 81:105]=1
    if Place[Place==2].size==0:
        img_whole[81:105, 55:79]=1
    if Place[Place==3].size==0:
        img_whole[81:105, 81:105]=1
    
    f_2_tensor=torch.from_numpy(att_out).float()
    img_out=forward_f_2(model_vae1,f_2_tensor).detach().numpy()[0,0,:,:]
    img_out = zoom(img_out, (160/80, 160/80))
    
    img_whole[img_whole>=0.999]=img_out[img_whole>=0.999]
    return img_whole

def draw_pic_leftright(att,att_2):
    ##load vae models
    with open('vae/bbvae_bvae.yaml', 'r') as file:
        config = yaml.safe_load(file)
    #data = VAEDataset(**config["data_params"], pin_memory=len(config['trainer_params']['gpus']) != 0)
    model_vae = BVAE(**config['model_params'])
    state_dict_vae=torch.load('log\\bvae\\leftright\\last.ckpt', map_location='cpu')
    state_dict_vae=state_dict_vae['state_dict']

    new_state_dict_vae=OrderedDict()
    for k,v in state_dict_vae.items():
        name=k[6:]
        new_state_dict_vae[name]=v

    model_vae.load_state_dict(new_state_dict_vae)
    model_vae=model_vae.eval()
    
    
    f_2_tensor=torch.from_numpy(att).float()
    img1=forward_f_2(model_vae,f_2_tensor).detach().numpy()[0,0,:,:]
    #img = zoom(img, (160/80, 160/80))
    
    f_2_tensor1=torch.from_numpy(att_2).float()
    img2=forward_f_2(model_vae,f_2_tensor1).detach().numpy()[0,0,:,:]
    #img1 = zoom(img1, (53/80, 53/80))
    img_whole=np.ones((160,160)) 
    img_whole[40:120, :80]=img1
    img_whole[40:120, 80:160]=img2
    img_whole[:,80]=0
    return img_whole

def draw_pic_updown(att,att_2):
    ##load vae models
    with open('vae/bbvae_bvae.yaml', 'r') as file:
        config = yaml.safe_load(file)
    #data = VAEDataset(**config["data_params"], pin_memory=len(config['trainer_params']['gpus']) != 0)
    model_vae = BVAE(**config['model_params'])
    state_dict_vae=torch.load('log\\bvae\\updown\\last.ckpt', map_location='cpu')
    state_dict_vae=state_dict_vae['state_dict']

    new_state_dict_vae=OrderedDict()
    for k,v in state_dict_vae.items():
        name=k[6:]
        new_state_dict_vae[name]=v

    model_vae.load_state_dict(new_state_dict_vae)
    model_vae=model_vae.eval()
    
    
    f_2_tensor=torch.from_numpy(att).float()
    img1=forward_f_2(model_vae,f_2_tensor).detach().numpy()[0,0,:,:]
    #img = zoom(img, (160/80, 160/80))
    
    f_2_tensor1=torch.from_numpy(att_2).float()
    img2=forward_f_2(model_vae,f_2_tensor1).detach().numpy()[0,0,:,:]
    #img1 = zoom(img1, (53/80, 53/80))
    img_whole=np.ones((160,160)) 
    img_whole[:80,40:120]=img1
    img_whole[80:160,40:120]=img2
    img_whole[80,:]=0
    return img_whole
    
    
    
    