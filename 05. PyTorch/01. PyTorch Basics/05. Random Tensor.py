import torch

random_tensor = torch.rand(3, 4)

print("Random Tensor:")
print(random_tensor)

print("\nShape:", random_tensor.shape)
print("Data Type:", random_tensor.dtype)
print("Minimum Value:", random_tensor.min().item())
print("Maximum Value:", random_tensor.max().item())