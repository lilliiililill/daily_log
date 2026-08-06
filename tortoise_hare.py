# 2026.08.06
# tortoise_hare.py

def next_number(n):

    return sum(int(digit) ** 2 for digit in str(n))

number = 8

slow = number
fast = next_number(number)

while fast != 1 and slow != fast:

    slow = next_number(slow)
    fast = next_number(next_number(fast))

print("행복한 수" if fast == 1 else "행복하지 않은 수")

