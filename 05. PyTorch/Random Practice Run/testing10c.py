# Reshaping and Flattening Tensors in PyTorch
# Reshaping a tensor means changing its shape without changing its data. In PyTorch, you can use the `reshape()` method to achieve this. The new shape must be compatible with the original shape, meaning that the total number of elements must remain the same.

import torch

x = torch.arange(12)

print("Original:")
print(x)
print(x.shape)

y = x.reshape(3, 4)

print("Reshaped:")
print(y)
print(y.shape)

# Flattening a tensor means converting it into a one-dimensional tensor. In PyTorch, you can use the `flatten()` method to achieve this. You can also specify the starting dimension from which to flatten the tensor.

x = torch.rand(2, 3, 4)

print("Original:", x.shape)

print("Flatten:", x.flatten().shape)

print("Flatten from dim 1:", x.flatten(start_dim=1).shape)