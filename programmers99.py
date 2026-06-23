# 2026.06.23
# programmers99.py

def solution(num, total):
    
    start = (total - num * (num - 1) // 2) // num
    
    return [start + i for i in range(num)]
