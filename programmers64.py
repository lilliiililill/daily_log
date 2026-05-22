# 2026.05.22
# programmers64.py

def solution(s1, s2):
    
    answer = 0
    
    for i in s1:
        
        if i in s2:
            
            answer += 1
    
    return answer
