# 2026.10.02
# even_digit_counter.py

def count_even_digits(n):

    return sum(1 for digit in str(abs(n)) if int(digit) % 2 == 0)

print(count_even_digits(482731))
