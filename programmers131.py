# 2026.07.14
# programmers131.py

def solution(arr, queries):
    
    answer = []
    
    for x, y, z in queries:
        
        for i in range(x, y+1):
            
            if i % z == 0:
                
                arr[i] = arr[i] + 1
    
    return arr
