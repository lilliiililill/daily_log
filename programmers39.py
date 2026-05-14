# 2026.05.14
# programmers39.py

def solution(numbers, k):
    answer = numbers[((k - 1) * 2) % len(numbers)]
    return answer
