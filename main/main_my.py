from math import sqrt

TypEr = "Посмотри, что ты вводишь?"

def func(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")
    return  result

def square_equation_solver(a, b, c):
    if not all(map(lambda p: isinstance(p, (int, float)), (a, b, c))):
        raise TypeError(TypEr)
    if a == 0:
        if b == 0:
            return None, None
        return -c / b, None
    d = b ** 2 - 4 * a * c
    if d < 0:
        return None, None
    d_sqrt = sqrt(d)
    x1 = (-b - d_sqrt) / 2*a
    x2 = (-b + d_sqrt) / 2*a
    if d == 0:
        x2 = None
    elif x2 > x1:
        x1, x2 = x2, x1
    return x1, x2

def func1(a):
    if not isinstance(a, str):
        return (2 / a), 2
    else:
        raise ValueError("Здесь есть ошибка!")