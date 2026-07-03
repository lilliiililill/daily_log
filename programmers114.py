# 2026.07.03
# programmers114.py

def solution(a, b):
    
    x = int(str(a) + str(b))
    y = int(str(b) + str(a))
    
    if x > y:
        
        answer = x
        
    elif y > x:
        
        answer = y
        
    else : 
        
        answer = x
    
    return answer
