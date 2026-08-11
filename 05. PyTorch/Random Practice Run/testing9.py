import torch

A = torch.tensor([
    [1, 2],
    [3, 4]
])

B = torch.tensor([
    [5, 6],
    [7, 8]
])

C = A @ B

print(C)
print((A @ B).shape)

# Rememeber:
# A * B - it's element-wise multiplication
# A @ B - it's matrix multiplication
# torch.matmul(A, B) - another way to do matrix multiplication
# another way to do matrix multiplication is torch.mm(A, B)