# 2026.08.15
# programmers179.py

def solution(myString):
    
    answer = []
    
    for i in myString:
        
        if i == 'a' or i == 'A':
            
            answer.append(i.upper())
            
        else:
            
            if i.isupper() == True:
                
                answer.append(i.lower())
                
            else:
                
                answer.append(i)
    
    return ''.join(answer)
