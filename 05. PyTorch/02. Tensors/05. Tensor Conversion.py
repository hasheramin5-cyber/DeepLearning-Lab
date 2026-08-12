import torch

tensor = torch.tensor([1, 2, 3, 4])

print("Original Tensor:")
print(tensor)
print("Original Data Type:", tensor.dtype)

float_tensor = tensor.float()

print("\nConverted Tensor:")
print(float_tensor)
print("Converted Data Type:", float_tensor.dtype)

int_tensor = float_tensor.int()

print("\nConverted Back to Integer:")
print(int_tensor)
print("Data Type:", int_tensor.dtype)