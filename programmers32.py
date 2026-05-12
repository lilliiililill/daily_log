# 2026.05.12
# programmers32.py

def solution(n):
    
    answer = len([(i, n // i) for i in range(1, n+1) if n % i == 0])
    
    return answer
