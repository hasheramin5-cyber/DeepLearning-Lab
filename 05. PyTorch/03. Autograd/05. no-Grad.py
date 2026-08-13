import torch

x = torch.tensor(5.0, requires_grad=True)

y = x ** 2

print("Before disabling gradient tracking:")
print("Requires Gradient:", x.requires_grad)
print("Output:", y)

with torch.no_grad():
    z = x ** 2

print("\nInside no_grad() context:")
print("Output:", z)
print("Requires Gradient:", z.requires_grad)