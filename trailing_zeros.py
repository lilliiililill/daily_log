# 2027.11.01
# trailing_zeros.py

def trailing_zeros(n):

    count = 0

    while n >= 5:

        n //= 5
        count += n

    return count

print(trailing_zeros(10))
print(trailing_zeros(25))
print(trailing_zeros(100))
