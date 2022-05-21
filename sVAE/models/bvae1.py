import torch
from models import BaseVAE
from torch import nn
from torch.nn import functional as F
from .types_ import *


class BVAE1(BaseVAE):

    num_iter = 0 # Global static variable to keep track of iterations

    def __init__(self,
                 in_channels: int,
                 latent_dim: int,
                 hidden_dims: List = None,
                 beta: int = 4,
                 gamma:float = 1000.,
                 max_capacity: int = 25,
                 Capacity_max_iter: int = 1e5,
                 loss_type:str = 'B',
                 **kwargs) -> None:
        super(BVAE1, self).__init__()

        self.latent_dim = latent_dim
        self.beta = beta
        self.gamma = gamma
        self.loss_type = loss_type
        self.C_max = torch.Tensor([max_capacity])
        self.C_stop_iter = Capacity_max_iter

        modules = []
        if hidden_dims is None:
#             hidden_dims = [32, 64, 128, 256, 512]
#              hidden_dims = [40, 64, 128, 256, 512]
            hidden_dims = [64,128,256]


        # Build Encoder
#         for h_dim in hidden_dims:
#             modules.append(
#                 nn.Sequential(
#                     nn.Conv2d(in_channels, out_channels=h_dim,
#                               kernel_size= 3, stride= 2, padding  = 1),
#                     nn.BatchNorm2d(h_dim),
#                     nn.LeakyReLU())
#             )
#             in_channels = h_dim

#         self.encoder = nn.Sequential(*modules)
#         self.fc_mu = nn.Linear(hidden_dims[-1]*9, latent_dim)
#         self.fc_var = nn.Linear(hidden_dims[-1]*9, latent_dim)
        self.fc_mu = nn.Linear(24*24, latent_dim)
        self.fc_var = nn.Linear(24*24, latent_dim)
#         self.fc_mu = nn.Linear(4608, latent_dim)
#         self.fc_var = nn.Linear(4608, latent_dim)

        self.f1=nn.Linear(latent_dim, 4096)
        self.f2=nn.Linear(4096, 29)
        self.f3=nn.Linear(29, 4096)
        self.f4=nn.Linear(4096, latent_dim)
        

        # Build Decoder
        modules = []
        self.decoder_input = nn.Linear(latent_dim, 24*24)
#         self.decoder_input = nn.Linear(latent_dim, hidden_dims[-1]*9)
# #         self.decoder_input = nn.Linear(latent_dim, 4608)
    
#         hidden_dims.reverse()

#         for i in range(len(hidden_dims) - 1):
#             modules.append(
#                 nn.Sequential(
#                     nn.ConvTranspose2d(hidden_dims[i],
#                                        hidden_dims[i + 1],
#                                        kernel_size=3,
#                                        stride = 2,
#                                        padding=1,
#                                        output_padding=1),
#                     nn.BatchNorm2d(hidden_dims[i + 1]),
#                     nn.LeakyReLU())
#             )



#         self.decoder = nn.Sequential(*modules)

#         self.final_layer = nn.Sequential(
#                             nn.ConvTranspose2d(hidden_dims[-1],
#                                                hidden_dims[-1],
#                                                kernel_size=3,
#                                                stride=2,
#                                                padding=1,
#                                                output_padding=1),
#                             nn.BatchNorm2d(hidden_dims[-1]),
#                             nn.LeakyReLU(),
#                             nn.Conv2d(hidden_dims[-1], out_channels= 1,
#                                       kernel_size= 3, padding= 1),
#                             nn.Tanh())
#         self.final_layer = nn.Sequential(
#                             nn.ConvTranspose2d(32,
#                                                80,
#                                                kernel_size=3,
#                                                stride=2,
#                                                padding=1,
#                                                output_padding=1),
#                             nn.BatchNorm2d(80),
#                             nn.LeakyReLU(),
#                             nn.Conv2d(80, out_channels= 3,
#                                       kernel_size= 3, padding= 1),
#                             nn.Tanh())

    def encode(self, input: Tensor) -> List[Tensor]:
        """
        Encodes the input by passing through the encoder network
        and returns the latent codes.
        :param input: (Tensor) Input tensor to encoder [N x C x H x W]
        :return: (Tensor) List of latent codes
        """
#         result = self.encoder(input)
#         #print(input.size())
#         #print(result.size())
#         result = torch.flatten(result, start_dim=1)
        result = torch.flatten(input, start_dim=1)
        #print(result.size())

        # Split the result into mu and var components
        # of the latent Gaussian distribution
        mu = self.fc_mu(result)
        log_var = self.fc_var(result)

        return [mu, log_var]

    def decode(self, z: Tensor) -> Tensor:
        result = self.decoder_input(z)
        #print(result.size())
        #result = result.view(-1, 512, 2, 2)
        #result = result.view(-1, 512, 3, 3)
#         result = result.view(-1, 256, 3, 3)
        result = result.view(-1,1,24,24)
        #print(result.size())
#         result = self.decoder(result)
#         #print(result.size())
#         result = self.final_layer(result)
        #print(result.size())
        return result

    def reparameterize(self, mu: Tensor, logvar: Tensor) -> Tensor:
        """
        Will a single z be enough ti compute the expectation
        for the loss??
        :param mu: (Tensor) Mean of the latent Gaussian
        :param logvar: (Tensor) Standard deviation of the latent Gaussian
        :return:
        """
        std = torch.exp(0.5 * logvar)
        eps = torch.randn_like(std)
        return eps * std + mu

    def forward(self, input: Tensor, **kwargs) -> Tensor:
        #print(kwargs['labels'])
        labels = kwargs['labels']
        mu, log_var = self.encode(input)
        f_1=self.f1(mu)
        f_2=self.f2(f_1)#feature
        f_3=self.f3(f_2)
        f_4=self.f4(f_3)
        z1 = self.reparameterize(mu, log_var)
        z2 = self.reparameterize(f_4, log_var)
        
        #print(self.decode(z).size())
        #return  [self.decode(z2), input, mu, log_var,f_2,z1,z2,labels]
        return  [self.decode(f_4), input, mu, log_var,f_2,mu,f_4,labels]

    def loss_function(self,
                      *args,
                      **kwargs) -> dict:
        self.num_iter += 1
        recons = args[0]
        input = args[1]
        mu = args[2]
        log_var = args[3]
        f_2=args[4]
        z1=args[5]
        z2=args[6]
        labels=args[7]
        
        kld_weight = kwargs['M_N']  # Account for the minibatch samples from the dataset
        
        recons_loss =F.mse_loss(recons, input)
        recons_z_loss=F.mse_loss(z1, z2)
#         feature_loss=F.mse_loss(f_2, labels.float()*10.)
        feature_loss=F.smooth_l1_loss(labels.float(), f_2, reduction = 'sum')
        
#         print(recons.dtype)
#         print(input.dtype)
#         print(z1.dtype)
#         print(z2.dtype)
#         print(f_2.dtype)
#         print(labels.dtype)
#         print(feature_loss.dtype)
#         print(recons_z_loss.dtype)
#         print(recons_loss.dtype)
        
        

        kld_loss = torch.mean(-0.5 * torch.sum(1 + log_var - mu ** 2 - log_var.exp(), dim = 1), dim = 0)

        if self.loss_type == 'H': # https://openreview.net/forum?id=Sy2fzU9gl
            loss = recons_loss + self.beta * kld_weight * kld_loss
        elif self.loss_type == 'B': # https://arxiv.org/pdf/1804.03599.pdf
            self.C_max = self.C_max.to(input.device)
            C = torch.clamp(self.C_max/self.C_stop_iter * self.num_iter, 0, self.C_max.data[0])
#             loss = recons_loss + self.gamma * kld_weight* (kld_loss - C).abs()
            loss = recons_loss + recons_z_loss + feature_loss + self.gamma * kld_weight* (kld_loss - C).abs()
#             if loss>=2:
#                 loss+=2000
#             else:
#                 loss+= feature_loss
        else:
            raise ValueError('Undefined loss type.')
            
        
        #los={'loss': loss, 'Reconstruction_Loss':recons_loss, 'KLD':kld_loss}

        return {'loss': loss, 'Reconstruction_Loss':recons_loss, 'KLD':kld_loss}
#         return loss,acc

    def sample(self,
               num_samples:int,
               current_device: int, **kwargs) -> Tensor:
        """
        Samples from the latent space and return the corresponding
        image space map.
        :param num_samples: (Int) Number of samples
        :param current_device: (Int) Device to run the model
        :return: (Tensor)
        """
#         z = torch.randn(num_samples,
#                         self.latent_dim)

#         z = z.to(current_device)
        f_2 = torch.randn(num_samples,
                        29)

        f_2 = f_2.to(current_device)
        
        f_3=self.f3(f_2)
        f_4=self.f4(f_3)
        
        #z2 = self.reparameterize(f_4, log_var)
        

        samples = self.decode(f_4)
        return samples

    def generate(self, x: Tensor, **kwargs) -> Tensor:
        """
        Given an input image x, returns the reconstructed image
        :param x: (Tensor) [B x C x H x W]
        :return: (Tensor) [B x C x H x W]
        """
        test_labels=kwargs['labels']

        return self.forward(x,labels=test_labels)[0]
    
   