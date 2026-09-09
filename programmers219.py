# 2026.09.09
# programmers219.py

def solution(myString):
    
    answer = []
    
    for i in myString:
        
        if i < "l":
            
            answer.append("l")
            
        else:
            
            answer.append(i)
    
    return "".join(answer)
