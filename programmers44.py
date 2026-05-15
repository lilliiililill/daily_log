# 2026.05.15
# programmers44.py

def solution(n):
    
    answer = 1
    factorial = 1
    
    while factorial <= n:
        
        answer += 1
        factorial *= answer
    
    return answer - 1
