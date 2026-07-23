# 2026.07.23
# programmers147.py

def solution(my_string, is_prefix):
    
    my_list = list(my_string)
    answer = []
    
    for i in range(0,len(my_list)):
        
        answer.append("".join(my_list[:i]))
        
    if is_prefix in answer:
        
        return 1
    
    else:
        
        return 0
