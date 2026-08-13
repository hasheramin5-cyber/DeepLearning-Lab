import torch

x = torch.tensor(5.0, requires_grad=True)

y = x ** 2

print("Input:", x)
print("Requires Gradient:", x.requires_grad)
print("Output:", y)