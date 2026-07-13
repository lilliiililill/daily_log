# 2026.07.13
# programmers129.py

def solution(arr, queries):
    
    for x, y in queries:
        
        arr[x], arr[y] = arr[y], arr[x]
    
    return arr
