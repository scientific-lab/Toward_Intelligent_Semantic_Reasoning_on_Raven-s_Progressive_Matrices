import torch 
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
from dataset_for_7_classes_train import d7class


# Device configuration
device = torch.device('cuda:1' if torch.cuda.is_available() else 'cpu')

# Hyper parameters
num_epochs = 50
num_classes = 7
batch_size = 512
learning_rate = 0.001

# MNIST dataset
train_transforms = transforms.Compose([transforms.ToTensor(),])
        
val_transforms = transforms.Compose([transforms.ToTensor(),])

train_dataset = d7class(
    split='train',
    transform=train_transforms,
    download=False,
)

# Replace CelebA with your dataset
val_dataset = d7class(
    split='test',
    transform=val_transforms,
    download=False,
)

#     train_set = torchvision.datasets.CIFAR10(
#         root='./data', train=True, download=True, transform=transform
#     )
#     train_loader = torch.utils.data.DataLoader(
#         train_set, batch_size=args.batch_size, shuffle=True, num_workers=2
#     )
#     test_set = torchvision.datasets.CIFAR10(
#         root='./data', train=False, download=True, transform=transform
#     )
#     test_loader = torch.utils.data.DataLoader(
#         test_set, args.test_batch_size, shuffle=False, num_workers=2
#     )
train_loader = torch.utils.data.DataLoader(
        train_dataset,
        batch_size=batch_size,
        num_workers=2,
        shuffle=True,
    )
test_loader = torch.utils.data.DataLoader(
        val_dataset,
        batch_size=batch_size,
        num_workers=2,
        shuffle=False,
    )

# Convolutional neural network (two convolutional layers)
class ConvNet(nn.Module):
    def __init__(self, num_classes=10):
        super(ConvNet, self).__init__()
        self.layer1 = nn.Sequential(
            nn.Conv2d(1, 16, kernel_size=5, stride=1, padding=2),
            nn.BatchNorm2d(16),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2))
        self.layer2 = nn.Sequential(
            nn.Conv2d(16, 32, kernel_size=5, stride=1, padding=2),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2))
        self.layer3 = nn.Sequential(
            nn.Conv2d(32, 64, kernel_size=5, stride=1, padding=2),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2))
        self.layer4 = nn.Sequential(
            nn.Conv2d(64, 128, kernel_size=5, stride=1, padding=2),
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2))
        
#         self.fc = nn.Linear(12800, 16384)
        #self.fc = nn.Linear(12800, num_classes)
        self.fc = nn.Linear(12800, 16384)
        self.fc1 = nn.Linear(16384, num_classes)
        
    def forward(self, x):
        #print(x.shape)
        #print(x)
        out = self.layer1(x)
        #print(out.shape)
        out = self.layer2(out)
        #print(out.shape)
        out = self.layer3(out)
        out = self.layer4(out)
        #print(out.shape)
        out = out.reshape(out.size(0), -1)
        #print(out.shape)
        out = self.fc(out)
        out = self.fc1(out)
        #out = self.fc1(out)
        #print(out.shape)
        return out

model = ConvNet(num_classes).to(device)

# Loss and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

# Train the model
total_step = len(train_loader)
for epoch in range(num_epochs):
    for i, (images, labels) in enumerate(train_loader):
        images=images.float()
        images = images.to(device)
        labels = labels.to(device)
        
        # Forward pass
        outputs = model(images)
        loss = criterion(outputs, labels)
        
        # Backward and optimize
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        if (i+1) % 100 == 0:
            print ('Epoch [{}/{}], Step [{}/{}], Loss: {:.4f}' 
                   .format(epoch+1, num_epochs, i+1, total_step, loss.item()))

    # Test the model
    model.eval()  # eval mode (batchnorm uses moving mean/variance instead of mini-batch mean/variance)
    with torch.no_grad():
        correct = 0
        total = 0
        for images, labels in test_loader:
            images=images.float()
            images = images.to(device)
            labels = labels.to(device)
            outputs = model(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

        print('Test Accuracy of the model: {} %'.format(100 * correct / total))

    # Save the model checkpoint
    torch.save(model.state_dict(), 'log1/model'+str(epoch)+'.ckpt')