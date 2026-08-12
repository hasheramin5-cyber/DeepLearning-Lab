import torch
import numpy as np

numpy_array = np.array([10, 20, 30, 40, 50])

tensor = torch.from_numpy(numpy_array)

print("NumPy Array:")
print(numpy_array)
print("NumPy Data Type:", numpy_array.dtype)

print("\nPyTorch Tensor:")
print(tensor)
print("Tensor Data Type:", tensor.dtype)

numpy_array[0] = 100

print("\nAfter modifying NumPy Array:")
print("NumPy Array:", numpy_array)
print("PyTorch Tensor:", tensor)