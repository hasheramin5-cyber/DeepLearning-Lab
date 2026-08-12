import torch

print("\nPyTorch Version Information")
print("-" * 35)

version = torch.__version__

print("Installed Version :", version)

major, minor = version.split(".")[:2]

print("Major Version     :", major)
print("Minor Version     :", minor)

if "+" in version:
    build = version.split("+")[1]
else:
    build = "Stable Release"

print("Build Type        :", build)

print("\nPyTorch is ready for Deep Learning!\n")