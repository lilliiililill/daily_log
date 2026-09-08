# 2026.09.08
# programmers217.py

def solution(picture, k):
    
    answer = []
    
    for row in picture:
        
        new_row = "".join(c * k for c in row)
        
        for _ in range(k):
            
            answer.append(new_row)

    
    return answer
