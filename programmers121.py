# 2026.07.08
# programmers121.py

def solution(code):
    
    mode = 0
    answer = []
    
    for idx, ch in enumerate(code):
        
        if ch == "1":
            
            if mode == 0:
                
                mode = 1
                
            else:
                
                mode = 0
                
        else:
            
            if mode == 0 and idx % 2 == 0:
                
                answer.append(ch)
                
            if mode == 1 and idx % 2 == 1:
                
                answer.append(ch)
                
    if len(answer) == 0:
        
        return "EMPTY"

    else:
        
        return ''.join(answer)
                
    
