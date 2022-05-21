import os
import torch
import numpy as np
from torch import Tensor
from pathlib import Path
from typing import List, Optional, Sequence, Union, Any, Callable
from torchvision.datasets.folder import default_loader
from pytorch_lightning import LightningDataModule
from torch.utils.data import DataLoader, Dataset
from torchvision import transforms
from torchvision.datasets import CelebA
import zipfile

class d7class(Dataset):
    """
    URL = https://www.robots.ox.ac.uk/~vgg/data/pets/
    """
    def __init__(self, 
                 split: str,
                 transform: Callable,
                **kwargs):
        
        
#         self.data_dir1 = Path('\center_single')        
        self.transforms = transform
#         imgs = sorted([f for f in self.data_dir.iterdir()])
        
#         self.imgs = imgs[:int(len(imgs) * 0.75)] if split == "train" else imgs[int(len(imgs) * 0.75):]
        
#         self.label_dir=Path(data_path) / "twobytwo_att_2" 
#         label = sorted([f for f in self.label_dir.iterdir()])
        
#         self.label = label[:int(len(label) * 0.75)] if split == "train" else label[int(len(label) * 0.75):]
#         #print(self.imgs)
        Name1 =os.listdir('center_single') 
        Name2 =os.listdir('distribute_four') 
        Name3 =os.listdir('distribute_nine') 
        Name4 =os.listdir('in_center_single_out_center_single') 
        Name5 =os.listdir('in_distribute_four_out_center_single') 
        Name6 =os.listdir('left_center_single_right_center_single') 
        Name7 =os.listdir('up_center_single_down_center_single') 
        P=['center_single','distribute_four','distribute_nine','in_center_single_out_center_single','in_distribute_four_out_center_single','left_center_single_right_center_single','up_center_single_down_center_single']

        question=[]
        answer=[]
        k=0
        for Name in [Name1,Name2,Name3,Name4,Name5,Name6,Name7]:
            for i in range (0,959):
            #for i in [0,1]:
                length=len('RAVEN_'+str(i)+'_')
                for j in range (0,len(Name1)):
                    if Name1[j][0:length]=='RAVEN_'+str(i)+'_' and Name1[j][-4:]=='.npz':
                        question.append(Path(P[k]) / Name1[j])
                        answer.append(k)
            k+=1
        if os.path.exists('sort.npy'):
            sort=np.load('sort.npy')
        else:
            sort= np.random.permutation(np.arange(len(question)))
            np.save('sort.npy',sort)
        question1=question.copy()
        answer1=answer.copy()
        for i in range (0,len(question)):
            question1[i]=question[sort[i]]
            answer1[i]=answer[sort[i]]
        
        imgs=question1
        label=answer1
        
        self.imgs = imgs[:int(len(imgs) * 0.75)] if split == "train" else imgs[int(len(imgs) * 0.75):]
        self.label = label[:int(len(label) * 0.75)] if split == "train" else label[int(len(label) * 0.75):]
        
        
    
    def __len__(self):
        return len(self.imgs)
    
    def __getitem__(self, idx):
        #img = np.load(self.imgs[idx])
        #img1=np.zeros((160,160,3))
        img = np.load(self.imgs[idx])['image'][0,:,:]
#         for i in range (0,3):
#             img1[:,:,i]=img
#         img = np.load('Data/twobytwo/34459.npy')
#         label=np.zeros(7)
#         label[self.label[idx]]=1
        label=self.label[idx]
        
        if self.transforms is not None:
            img = self.transforms(img)
        
        return img, label # dummy datat to prevent breaking 