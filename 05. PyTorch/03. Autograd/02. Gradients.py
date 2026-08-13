import torch

x = torch.tensor(5.0, requires_grad=True)

y = x ** 2

y.backward()

print("Input:", x)
print("Output:", y)
print("Gradient:", x.grad)