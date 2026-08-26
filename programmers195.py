# 2026.08.26
# programmers195.py

def solution(arr, k):
    
    answer = []
    
    for i in arr:
        
        if i not in answer:
            
            answer.append(i)
            
    if len(answer) < k:
        
        while len(answer) < k:
            
            answer.append(-1)
            
    else:
        
        while len(answer) != k:
            
            del answer[-1]
            
            
    return answer
    
    
