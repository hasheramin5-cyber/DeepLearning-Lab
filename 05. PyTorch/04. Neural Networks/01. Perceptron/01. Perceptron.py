
import torch

x = torch.tensor([1.0, 0.0])

weights = torch.tensor([0.5, -0.5])

bias = torch.tensor(0.2)

weighted_sum = torch.sum(x * weights) + bias

if weighted_sum >= 0:
    prediction = 1
else:
    prediction = 0

print("Input:", x)
print("Weights:", weights)
print("Bias:", bias)
print("Weighted Sum:", weighted_sum)
print("Prediction:", prediction)