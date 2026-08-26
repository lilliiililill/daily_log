# 2026.08.26
# programmers194.py

def solution(arr):
    
    answer = []
    i = 0
    
    while i < len(arr):
        
        if not answer:
            
            answer.append(arr[i])
            i += 1
            
        elif answer and answer[-1] == arr[i]:
            
            del answer[-1]
            i += 1
            
        elif answer and answer[-1] != arr[i]:
            
            answer.append(arr[i])
            i += 1
            
    if not answer:
        
        answer.append(-1)
    
    return answer
