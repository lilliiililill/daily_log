# 2026.07.10
# programmers128.py

def solution(numLog):
    
    answer = []
    
    prev = numLog[0]
    
    for i in numLog[1:]:
        
        if i - prev == 1:
            
            answer.append("w")
            
        elif i - prev == -1:
            
            answer.append("s")
        
        elif i - prev == 10:
            
            answer.append("d")
            
        elif i - prev == -10:
            
            answer.append("a")
            
        prev = i
    
    return ''.join(answer)
