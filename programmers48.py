# 2026.05.18
# programmers48.py

def solution(n):
    
    i = 2
    answer = []
    
    while i * i <= n:
        
        if n % i != 0:
            
            i += 1
            
        else:
            
            n //= i
            answer.append(i)
            
            
    if n > 1:
        
        answer.append(n)
        
    answer = list(set(answer))
    answer.sort()
        
    return answer
