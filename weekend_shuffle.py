# 2026.08.08
# weekend_shuffle.py

numbers = [3, 1, 4, 1, 5, 9, 2, 6]

result = []

while numbers:

    smallest = min(numbers)
    result.append(smallest)
    numbers.remove(smallest)

print(result)
