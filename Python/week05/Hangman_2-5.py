#A program to find differentiation


def f(x):
    return x*x + 2*x + 1

def derivative(x):
    h = 0.0001
    numerator = f(x + h) - f(x)
    denominator = h
    return numerator / denominator


print("Type x point\n")

x = float(input())


result = derivative(x)
print("The derivative of ", x, "is approximately:", result)
