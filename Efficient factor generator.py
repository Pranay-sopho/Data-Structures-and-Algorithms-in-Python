def factors(n):
    i = 1
    while i * i < n:
        if n % i == 0:
            yield i
            yield n // i
        i += 1
    if i * i == n:
        yield i

for factor in factors(100):
    print(factor)