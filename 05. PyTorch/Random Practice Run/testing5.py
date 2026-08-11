import torch

x = torch.rand(4, 5, 3)

print(f"X-Tensor:\n {x}")

print(f"Shape of X: {x.shape}")
print(f"Numbers of Element in X-Tensor: {x.numel()}") 
# will show the numbers of elements in the X-tensor

print("Shape:")

print(x.shape,
      x[2].shape,
      x[2, 3].shape,
      x[2, 3, 1].shape)


'''

torch.rand(A, B, C, D)
(A, B, C, D)

 _____________________________________
|  Batch x Channels x Height x Width  |
|   |        |          |       |     |
|   |        |          |       |     |
|   32  x    3     x   224  x  224    |
|_____________________________________|

32  → images ki quantity
3   → channels (RGB)
224 → height
224 → width

'''