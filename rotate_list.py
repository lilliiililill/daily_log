# 2026.10.01
# rotate_list.py

numbers = [1, 2, 3, 4, 5]

shift = 2

shift %= len(numbers)

rotated = numbers[-shift:] + numbers[:-shift]

print(rotated)
