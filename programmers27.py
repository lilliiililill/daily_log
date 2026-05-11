# 2026.05.11
# programmers27.py

def solution(n, k):
    
    bever = int(n * 0.1)
    answer = (n * 12000) + ((k - bever) * 2000)
    return answer
