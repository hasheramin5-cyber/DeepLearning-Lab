import torch

zeros_tensor = torch.zeros(3, 4)
ones_tensor = torch.ones(3, 4)

print("Zeros Tensor:")
print(zeros_tensor)

print("\nOnes Tensor:")
print(ones_tensor)

print("\nZeros Tensor Shape:", zeros_tensor.shape)
print("Ones Tensor Shape:", ones_tensor.shape)

print("\nZeros Tensor Data Type:", zeros_tensor.dtype)
print("Ones Tensor Data Type:", ones_tensor.dtype)