# Build a simple Perceptron using PyTorch tensors.

import torch

# Input features for one sample.
x = torch.tensor([1.0, 0.0])

# Weight assigned to each input feature.
weights = torch.tensor([0.5, -0.5])

# Bias shifts the decision boundary.
bias = torch.tensor(0.2)

# Calculate the weighted sum.
weighted_sum = torch.sum(x * weights) + bias

# Apply a simple step activation.
if weighted_sum >= 0:
    prediction = 1
else:
    prediction = 0

print("Input:", x)
print("Weights:", weights)
print("Bias:", bias)
print("Weighted Sum:", weighted_sum)
print("Prediction:", prediction)

# Explanation:
# A perceptron multiplies each input by its weight and adds the bias.
# The resulting weighted sum is passed through a step function.
# A non-negative value produces class 1, otherwise the output is class 0.