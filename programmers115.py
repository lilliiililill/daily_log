# 2026.07.04
# programmers115.py

def solution(a, b):
    
    x = int(str(a) + str(b))
    y = 2 * a * b
    
    if x > y:
        
        answer = x
        
    elif y > x:
        
        answer = y
        
    else:
        
        answer = x
    
    return answer
