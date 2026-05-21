# 2026.05.21
# programmers58.py

def solution(my_string, num1, num2):
    
    my_list = list(my_string)
    
    a = my_list[num1]
    
    my_list[num1] = my_list[num2]
    my_list[num2] = a
    
    answer = ''.join(my_list)
    
    return answer
