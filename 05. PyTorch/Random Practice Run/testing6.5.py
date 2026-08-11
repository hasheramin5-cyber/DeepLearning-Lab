'''

Y[  :  ,  :  ,  :  ,  :  ]
    │     │     │     │
    │     │     │     └── all Width
    │     │     └──────── all Height
    │     └────────────── all Channels
    └──────────────────── all Images
    
# A vision for Computer Vision tensors


Y.shape = [32, 3, 224, 224]

             N    C    H    W
             │    │    │    │
             32 x 3 x 224 x 224


# Lock These Rules:

x[0]       → first matrix
x[:]       → all matrices

x[0, :]    → first matrix, all rows
x[:, 0]    → all matrices, first row

x[:, :, 0] → all matrices, all rows, first column

 ___________________________________
| [Batch, Channels, Height, Width]  |
|    N        C       H       W     |
|___________________________________|

'''

import torch

x = torch.rand(4, 5, 3)
y = torch.rand(32, 3, 224, 224)

print()
print(f"Shape of X-Tensor: {x.shape}")
print(f"Shape of Y-Tensor: {y.shape}")

print()
print(f"Dimension of X-Tensor: {x.ndim}D")
print(f"Dimension of Y-Tensor: {y.ndim}D")

print()
print(x[0])# First Matrix
print(y[0])

print()
print(x[:])
print(y[:])

print()
print(x[0, :],    # → first matrix, all rows of X
      x[:, 0])    # → all matrices, first row of X

print(y[0, :],    # → first matrix, all rows of Y
      y[:, 0])    # → all matrices, first row of Y

print()
print(x[:, :, 0]) # All matrix, all Row, First Columns
print(y[:, :, 0])