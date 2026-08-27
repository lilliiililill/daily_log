# 2026.08.27
# programmers196.py

def solution(arr):
    
    answer = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    
    while len(arr) < 1024:
        
        if len(arr) not in answer:
            
            arr.append(0)
        
        else:
            
            return arr
    
    return arr
