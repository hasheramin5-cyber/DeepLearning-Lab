import torch

x = torch.tensor([[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12],
                 [13, 14, 15, 16]])


# Slicing - Quadrants

print("\n\nSlicing - Quadrants")
print("\nTop-Left Quadrant:")
print(x[0:2,0:2])

print("\nTop-Right Quadrant:")
print(x[0:2,2:4]) # You can also Perform the Same Operation by --> x[0:2,2:]

print("\nBottom-Left Quadrant:")
print(x[2:4,0:2])

print("\nBottom-Right Quadrant:")
print(x[2:4,2:]) # You can also Perform the Same Operation by --> x[0:2,2:4]

print("\nCenter:")
print(x[1:3,1:3])

# Slicing - Randoms

print("\n\nSlicing - Randoms")
print("\nFirst Row Only:")
print(x[0:1,:])

print("\nLast Row Only:")
print(x[3:,:])

print("\nFirst Column Only:")
print(x[:,0:1])

print("\nLast Column Only:")
print(x[:,3:])

print("\nRandom:")
print(x[3:4,0:1])
print(x[2:3,2:4])
print(x[:1,:1])
print(x[1:2,2:3])