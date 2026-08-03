# 2026.08.03
# programmers159.py

def solution(arr):

    first = -1
    last = -1
    
    for i, num in enumerate(arr):
        
        if num == 2:
            
            if first == -1:
                
                first = i
                
            last = i
            
    if first == -1:
        
        return [-1]
    
    return arr[first:last + 1]
