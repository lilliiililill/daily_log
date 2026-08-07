# 2026.08.07
# programmers167.py

def solution(names):
    
    answer = []
    
    for idx, value in enumerate(names):
        
        if idx % 5 == 0:
            
            answer.append(value)
    
    return answer
