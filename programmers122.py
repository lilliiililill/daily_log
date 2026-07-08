# 2026.07.08
# programmers122.py

def solution(a, d, included):
    
    answer = 0
    
    for idx, check in enumerate(included):
        
        if check == True:
            
            answer += (a + d * idx)
    
    return answer
