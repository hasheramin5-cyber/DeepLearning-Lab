import torch

scalar = torch.tensor(10)

vector = torch.tensor([1, 2, 3, 4])

matrix = torch.tensor([[1, 2, 3],
                       [4, 5, 6]])

tensor_3d = torch.tensor([[[1, 2],[3, 4]],
                          [[5, 6],[7, 8]]])

print("Scalar dimensions:", scalar.ndim)
print("Vector dimensions:", vector.ndim)
print("Matrix dimensions:", matrix.ndim)
print("3D Tensor dimensions:", tensor_3d.ndim)