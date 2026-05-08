# 2026.05.08
# programmers18.py

def solution(money):
    
    answer = []
    
    if money < 5500:
        
        answer.append(0)
        answer.append(money)
        
    else:
        
        answer.append(money // 5500)
        answer.append(money % 5500)
        
    return answer
