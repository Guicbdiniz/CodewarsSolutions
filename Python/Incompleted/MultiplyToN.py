# Multiply to n - 4kyu


def prime_factors_of(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def multiply(n, k):
    if n == 1:
        return 1
    else:
        prime_factors = prime_factors_of(n)
        total_possibilities = k ** len(prime_factors)
        repetitions = {}
        for factor in prime_factors:
            if repetitions.get(factor):
                repetitions[factor] = repetitions[factor] + 1
            else:
                repetitions[factor] = 1
        for key, value in repetitions.items():
            if value > 1:
                total_possibilities -= k ** value
    return total_possibilities


print(multiply(36, 2))
