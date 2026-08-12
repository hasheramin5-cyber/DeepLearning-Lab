import torch

tensor = torch.tensor([
    [10, 20, 30],
    [40, 50, 60]
])

print("Tensor:")
print(tensor)

print("\nTensor Attributes")
print("Data Type:", tensor.dtype)
print("Device:", tensor.device)
print("Shape:", tensor.shape)
print("Dimensions:", tensor.ndim)
print("Number of Elements:", tensor.numel())