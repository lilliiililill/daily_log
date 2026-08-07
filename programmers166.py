# 2026.08.07
# programmers166.py

def solution(num_list):
    
    x = 0
    y = 0
    
    for idx, value in enumerate(num_list):
        
        if idx % 2 == 0:
            
            x += value
            
        else:
            
            y += value
            
    return max(x, y)
