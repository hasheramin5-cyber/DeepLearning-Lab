import torch

scalar = torch.tensor(10)

vector = torch.tensor([1, 2, 3, 4])

matrix = torch.tensor([[1, 2, 3],
                       [4, 5, 6]])

tensor_3d = torch.tensor([[[1, 2],[3, 4]],
                          [[5, 6],[7, 8]]])

print("Scalar shape:", scalar.shape)
print("Vector shape:", vector.shape)
print("Matrix shape:", matrix.shape)
print("3D Tensor shape:", tensor_3d.shape)