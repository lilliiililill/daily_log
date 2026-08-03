# 2026.08.03
# programmers160.py

def solution(arr, query):
    
    for i, q in enumerate(query):
        
        if i % 2 == 0:
            
            arr = arr[:q+1]
            
        else:
            
            arr = arr[q:]
    
    
    return arr
