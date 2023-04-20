#A program that prints the integral range

print('type integral range\n')

def f(x):
    return x*x + 2*x + 1

lower, upper = map(int, input().split())
#upper = int(input())
dx = 0.0001

n = int((upper - lower) / dx)
h = (upper - lower) / float(n)

integral = (f(lower) + f(upper)) / 2

for i in range(1, n):
    x = lower + i*h
    integral += f(x)

integral *= h

print("The integral of ", lower, ",", upper, " is approximately:", integral)

