# 2026.08.24
# programmers193.py

def solution(arr, flag):
    
    answer = []
    
    for a, b in zip(arr, flag):
        
        if b == True:
            
            for _ in range(0, a*2):
                
                answer.append(a)
                
        else:
            
            del answer[-a:]
    
    return answer
