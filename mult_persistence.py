# 2026.10.15
# mult_persistence.py

def mult_persistence(n):

    steps = 0

    while n >= 10:

        prod = 1

        while n > 0:

            prod *= n % 10
            n //= 10

        n = prod
        steps += 1

    return steps

print(mult_persistence(39))
print(mult_persistence(999))
