# 2026.07.31
# programmers158.py

def solution(arr, intervals):
    
    answer = []
    
    for x, y in intervals:
        
        for i in range(x, y+1):
            
            answer.append(arr[i])
    
    return answer
