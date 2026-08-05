# 2026.08.05
# programmers165.py

def solution(num_list, n):
    
    answer = []
    
    for i in range(0, len(num_list)):
        
        if i % n == 0:
            
            answer.append(num_list[i])
    
    return answer
