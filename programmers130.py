# 2026.07.13
# programmers130.py

def solution(arr, queries):
    
    result = []
    
    for s, e, k in queries:
        
        answer = []
        
        for i in range(s, e+1):
            
            if arr[i] > k:
                
                answer.append(arr[i])
            
        if answer:
            
            result.append(min(answer))
                
        else:
            
            result.append(-1)

    
    return result
