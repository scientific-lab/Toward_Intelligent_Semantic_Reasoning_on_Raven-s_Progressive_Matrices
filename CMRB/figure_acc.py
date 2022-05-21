from torchvision import transforms
import yaml
import torch
import numpy as np
from vae.bvae import BVAE
from collections import OrderedDict
from change_angle import change_att
def forward_to_f_2(model_vae,input, **kwargs):
    #print(kwargs['labels'])
    #labels = kwargs['labels']
    mu, log_var = model_vae.encode(input)
    f_1=model_vae.f1(mu)
    f_2=model_vae.f2(f_1)#feature

    #print(self.decode(z).size())
    return  f_2

# def compare(data,t):#twobytwo
    
#     img_tensor=transforms.functional.to_tensor(data)
#     f_2=forward_to_f_2(model_vae,img_tensor.reshape(1,1,80,80)).detach().numpy()
    
#     return f_2

for t in range (0,2):
#for t in [1]:
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
    a=0
    for i in range (0,36551):
        data=np.load('D:\\zsk\\RAVEN\\data_crop\\img\\'+str(i)+'.npy')
        img_tensor=transforms.functional.to_tensor(data)
        f_2=forward_to_f_2(model_vae,img_tensor.reshape(1,1,80,80)).detach().numpy()
        #f_2=compare(data,t)
        f_2=np.round(f_2)
        att=np.load('D:\\zsk\\RAVEN\\data_crop\\att\\'+str(i)+'.npy')
        att=change_att(att)
        #print(f_2[0][1])
        #print(att)
        if (f_2==att).all():
            #print('1')
            a+=1
    print(a/36551)