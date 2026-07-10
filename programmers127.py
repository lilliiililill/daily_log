# 2026.07.10
# programmers127.py

def solution(n, control):
    
    control_list = list(control)
    
    for i in control_list:
        
        if i == "w":
            
            n += 1
        
        elif i == "s":
            
            n -= 1
            
        elif i == "d":
            
            n += 10
            
        elif i == "a":
            
            n -= 10
            
    answer = n
    
    return answer
