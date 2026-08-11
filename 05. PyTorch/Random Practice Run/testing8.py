import torch

x = torch.tensor([2, 4, 6])
y = torch.tensor([3, 5, 7])

print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)

print("Scalar multiplication:", x * 10)
print("Scalar addition:", x + 10)

print(x @ y)
print(torch.matmul(x ,y))


# or we can also make it like this ...

x = torch.tensor([2, 4, 6])
y = torch.tensor([3, 5, 7])

print(torch.dot(x, y))


'''
First output value:
(1*5)+(2*7)=19

Second:
(1*6)+(2*8)=22

So:
[1  2]       [5  6]
[3  4]   @   [7  8]

       ↓

[19 22]
[43 50]

'''
