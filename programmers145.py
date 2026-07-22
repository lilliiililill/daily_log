# 2026.07.22
# programmers145.py

def solution(my_string, is_suffix):
    answer = []
    
    for i in range(1, len(my_string)+1):
        
        answer.append(my_string[-i:])
        
    if is_suffix in answer:
        
        return 1
    
    else:
        
        return 0
    
