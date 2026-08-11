import torch

x = torch.rand(2, 3)
y = torch.rand(3, 2)

z = torch.matmul(x, y)
print(z)
