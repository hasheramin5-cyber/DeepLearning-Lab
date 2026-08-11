# Slicing in PyTorch

import torch

x = torch.rand(4, 5, 3)

print(f"X-Tensor:\n {x}")
print()
print(f"Shape of X: {x.shape}")
print(f"Numbers of Element in X-Tensor: {x.numel()}")
print("Shape:")
print(x.shape,
      x[2].shape,
      x[2, 3].shape,
      x[2, 3, 1].shape)

print()
print("\nFirst Matrix:")
print(x[0])
print()
print(x[0, 1:4]) # Slicing the first matrix from index 1 to 3 (4 is exclusive)
print()

'''

        x[  :  ,  :  ,  :  ]
             │    │    │
             │    │    └── all columns
             │    └─────── all rows
             └──────────── all matrices
             
'''