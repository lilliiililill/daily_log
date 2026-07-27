# 2026.07.27
# programmers152.py

def solution(n, k):
    
    answer = []
    
    for i in range(1, n+1):
        
        if i % k == 0 : 
            
            answer.append(i)
    
    answer.sort()
    
    return answer
