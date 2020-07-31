# Product of consecutive Fib numbers - 5kyu


def productFib(product):
    a, b = 0, 1
    aux = 0
    while a * b < product:
        aux = a + b
        a = b
        b = aux
    return [a, b, a * b == product]
