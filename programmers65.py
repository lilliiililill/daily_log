# 2026.05.26
# programmers65.py

def solution(num, k):
    
    answer = 0
    num_list = list(str(num))
    
    if str(k) in num_list:
        
        answer = num_list.index(str(k)) + 1
        
    else:
        
        answer = -1
    
    return answer
