import torch

x = torch.rand(4, 5, 3)

print(f"X-Tensor:\n {x}")

print(f"Shape of X:\n {x.shape}")
print(f"Numbers of Element in X-Tensor:\n {x.numel()}") 
# will show the numbers of elements in the X-tensor

print("Shape:", x.shape)

print("\nFirst Matrix:")
print(x[0])

print("\nFirst Row:")
print(x[0, 0])

print("\nFirst Value:")
print(x[0, 0, 0])

print("\nLast Matrix:")
print(x[-1])

print("\nLast Value:")
print(x[-1, -1, -1])

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