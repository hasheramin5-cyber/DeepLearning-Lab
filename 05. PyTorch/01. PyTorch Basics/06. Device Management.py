import torch

# Select CUDA when a compatible GPU is available; otherwise use the CPU.
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

tensor = torch.tensor([10.0, 20.0, 30.0]).to(device)

print("Selected Device:", device)
print("Tensor:", tensor)
print("Tensor Device:", tensor.device)

if torch.cuda.is_available():
    print("GPU Name:", torch.cuda.get_device_name(0))
else:
    print("CUDA is not available. Using CPU.")