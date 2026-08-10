# 2026.08.10
# programmers169.py

def solution(numbers, n):
    
    answer = 0
    
    for i in numbers:
        
        if answer <= n:
            
            answer += i
            
        else:
            
            return answer
    
    return answer
