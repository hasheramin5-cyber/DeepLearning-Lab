import torch as tr

x = tr.tensor([
    [10.224, 20.42, 30.424],
    [40.5, 50.5, 60.5],
    [70.6, 80.6, 90.6]
])

print("Tensor:")
print(x)
print("\nShape:")
print(x.shape)
print("\nDimensions:")
print(x.ndim)
print("\nData Type:")
print(x.dtype)
print("\nDevice:")
print(x.device)