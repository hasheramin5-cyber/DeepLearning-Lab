import torch

x = torch.rand(4, 5, 3)

print("Original:", x.shape)

print("A:", x[0:2].shape)
print("B:", x[0, 1:4].shape)
print("C:", x[0, :, 0:2].shape)
print("D:", x[:, :, 0].shape)