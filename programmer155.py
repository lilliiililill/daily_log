# 2026.07.28
# programmer155.py

def solution(arr, idx):
    
    answer = 0
    
    for i, j in enumerate(arr):
        
        if i >= idx and j == 1:
            
            answer =  i
            break
            
        else:
            
            answer = -1
    
    return answer
