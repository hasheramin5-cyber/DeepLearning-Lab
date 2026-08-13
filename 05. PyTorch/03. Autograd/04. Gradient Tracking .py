import torch

x = torch.tensor(3.0, requires_grad=True)

y = x ** 2 + 2 * x + 1

print("Input:", x)
print("Output:", y)
print("Requires Gradient:", x.requires_grad)
print("Gradient Function:", y.grad_fn)

y.backward()

print("Gradient:", x.grad)