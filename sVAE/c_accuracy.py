import torch
from torch.nn import functional as F
def cal_acc(f_2,labels):
#     print(f_2.shape)
#     print(labels.shape)
    Pred1=F.softmax(f_2[:,0:5])
    Pred2=F.softmax(f_2[:,5:15])
    Pred3=F.softmax(f_2[:,15:21])
    Pred4=F.softmax(f_2[:,21:29])

    Label1=labels[:,0:5]
    Label2=labels[:,5:15]
    Label3=labels[:,15:21]
    Label4=labels[:,21:29]

    correct_pred1=torch.eq(Pred1.argmax(dim=1),Label1.argmax(dim=1))
    accuracy1=torch.mean(correct_pred1.float())

    correct_pred2=torch.eq(Pred2.argmax(dim=1),Label2.argmax(dim=1))
    accuracy2=torch.mean(correct_pred2.float())

    correct_pred3=torch.eq(Pred3.argmax(dim=1),Label3.argmax(dim=1))
    accuracy3=torch.mean(correct_pred3.float())
    
    correct_pred4=torch.eq(Pred4.argmax(dim=1),Label4.argmax(dim=1))
    accuracy4=torch.mean(correct_pred4.float())

    acc=(accuracy1+accuracy2+accuracy3+accuracy4)/4
    return acc