import torch


x = torch.tensor([[[33.33, 33.32, 33.31],[32.33, 32.32, 32.31],[31.33, 31.32, 31.31]],
                  [[30.33, 30.32, 30.31],[29.33, 29.32, 29.31],[28.33, 28.32, 28.31]],
                  [[27.33, 27.32, 27.31],[26.33, 26.32, 26.31],[25.33, 25.32, 25.31]]])


print(x)
print(torch.zeros(4, 5, 3))
print(torch.ones(4, 5, 3))
print(torch.rand(4, 5, 3))
print(torch.randn(4, 5, 3))
print(x.numel())
print(x.shape)
print(x.ndim)
print(x.dtype)
print(x.device)