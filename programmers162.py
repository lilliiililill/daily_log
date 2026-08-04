# 2026.08.04
# programmers162.py

def solution(num_list, n):
    
    answer = num_list[n:]
    
    for i in num_list[:n]:
        
        answer.append(i)
    
    
    return answer
