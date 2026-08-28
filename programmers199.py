# 2026.08.28
# programmers199.py

def solution(arr, n):
    
    if len(arr) % 2 == 1:
        
        for i in range(0, len(arr), 2):
            
            arr[i] += n
            
    else:
        
        for i in range(1, len(arr), 2):
            
            arr[i] += n
            
            
    
    return arr
