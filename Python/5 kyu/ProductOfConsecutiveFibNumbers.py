# Product of consecutive Fib numbers - 5kyu
# https://www.codewars.com/kata/5541f58a944b85ce6d00006a

# Access the link for a long task description.


def productFib(product):
    a, b = 0, 1
    aux = 0
    while a * b < product:
        aux = a + b
        a = b
        b = aux
    return [a, b, a * b == product]
