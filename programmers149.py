# 2026.07.24
# programmers149.py

def solution(my_string, m, c):
    
    answer = []
    
    my_list = list(my_string)
    
    chart_list = [my_list[i : i + m] for i in range(0, len(my_list), m)]
    
    for i in chart_list:
        
        answer.append(i[c - 1])
    
    return ''.join(answer)
