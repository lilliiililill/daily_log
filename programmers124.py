# 2026.07.09
# programmers124.py

import math

def solution(num_list):
    
    answer = 0
    a = 0
    b = 0
    
    if sum(num_list) ** 2 > math.prod(num_list):
        
        answer = 1
        
    else:
        
        answer = 0
    
    
    
    return answer
