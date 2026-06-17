# 2026.06.17
# programmers95.py

def solution(before, after):
    
    answer = 0
    
    if sorted(before) == sorted(after):
        
        answer = 1
        
    else:
        
        answer = 0
    
    return answer
