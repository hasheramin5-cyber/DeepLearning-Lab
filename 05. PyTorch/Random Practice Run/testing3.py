import torch

x = torch.rand(4, 5, 3)
y = torch.rand(32, 3, 224, 224)

print(f"X-Tensor:\n {x}")
print(f"Y-Tensor:\n {y}")
print()

print(f"Shape of X:\n {x.shape}")
print(f"Shape of Y:\n {y.shape}")
print(f"Numbers of Element in X-Tensor:\n {x.numel()}") # will show the numbers of elements in the X-tensor
print(f"Numbers of Element in Y-Tensor:\n {y.numel()}") # will show the numbers of elements in the Y-tensor


'''

torch.rand(A, B, C, D)
(A, B, C, D)


Batch x Channels x Height x Width
  |        |          |       |
  32  x    3     x   224  x  224


32  → images ki quantity
3   → channels (RGB)
224 → height
224 → width

'''