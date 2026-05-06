# 2026.05.06
# programmers12.py

def solution(n):
    answer = []
    
    for i in range(1, n+1):
        
        if i % 2 == 1:
            
            answer.append(i)
            
    return answer
