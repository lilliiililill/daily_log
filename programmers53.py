# 2026.05.20
# programmers53.py

def solution(array, n):
    
    answer = min(array, key=lambda x: (abs(x - n), x))
            
    return answer
