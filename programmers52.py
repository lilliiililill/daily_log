# 2026.05.19
# programmers52.py

def solution(sides):
    
    sides.sort()
    
    answer = 0
    
    if sides[0] + sides[1] <= sides[2]:
        
        answer = 2
        
    else:
        
        answer = 1
    
    return answer
