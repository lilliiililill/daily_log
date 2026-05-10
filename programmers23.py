# 2026.05.10
# programmers23.py

def solution(num_list):
    
    answer = []
    e_n = 0
    o_n = 0
    
    for i in num_list:
        
        if i % 2 == 0:
            
            e_n += 1
            
        else:
            
            o_n += 1
            
    answer.append(e_n)
    answer.append(o_n)
    
    return answer
