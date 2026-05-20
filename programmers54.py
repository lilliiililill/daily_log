# 2026.05.20
# programmers54.py

def solution(order):
    
    order_list = list(map(int, str(order)))
    
    answer = 0
    
    for i in order_list:
        
        if i in [3, 6, 9]:
            
            answer += 1
    
    return answer
