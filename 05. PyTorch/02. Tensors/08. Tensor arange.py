import torch

tensor = torch.arange(0, 10)

print("Tensor:")
print(tensor)

print("\nStart: 0")
print("End: 10")
print("Step: 1")

print("\nShape:", tensor.shape)
print("Data Type:", tensor.dtype)
print("Number of Elements:", tensor.numel())