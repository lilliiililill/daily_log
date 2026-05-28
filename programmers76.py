# 2026.05.28
# programmers76.py

def solution(array, height):
    
    answer = 0
    
    for i in array:
        
        if i > height:
            
            answer += 1
    
    return answer
