import torch

x = torch.tensor(4.0, requires_grad=True)

y = x ** 3

y.backward()

print("Input:", x)
print("Output:", y)
print("Gradient:", x.grad)