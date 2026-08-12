import torch

scalar = torch.tensor(7)

vector = torch.tensor([1, 2, 3, 4])

matrix = torch.tensor([[1, 2, 3],
                       [4, 5, 6]])

tensor_3d = torch.tensor([[[1, 2],[3, 4]],
                          [[5, 6],[7, 8]]])

print("Scalar:")
print(scalar)

print("\nVector:")
print(vector)

print("\nMatrix:")
print(matrix)

print("\n3D Tensor:")
print(tensor_3d)