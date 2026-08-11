# Reshape the tensor to a different shape

import torch

x = torch.tensor([
    [1, 2, 3],
    [4, 5, 6]
])

print("\nTensor Shape:", x.shape)
print(x)

x = x.reshape(3, 2)
print("\nReshaped Tensor Shape:", x.shape)
print(x)