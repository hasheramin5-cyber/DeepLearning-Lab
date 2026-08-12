import torch

integer_tensor = torch.tensor([1, 2, 3, 4])
float_tensor = torch.tensor([1.0, 2.0, 3.0, 4.0])
float32_tensor = torch.tensor([1, 2, 3, 4], dtype=torch.float32)
int64_tensor = torch.tensor([1, 2, 3, 4], dtype=torch.int64)

print("Integer Tensor:")
print(integer_tensor)
print("Data Type:", integer_tensor.dtype)

print("\nFloat Tensor:")
print(float_tensor)
print("Data Type:", float_tensor.dtype)

print("\nFloat32 Tensor:")
print(float32_tensor)
print("Data Type:", float32_tensor.dtype)

print("\nInt64 Tensor:")
print(int64_tensor)
print("Data Type:", int64_tensor.dtype)