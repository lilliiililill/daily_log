# 2026.07.23
# programmers148.py

def solution(my_string, s, e):
    
    my_list = list(my_string)
    answer = []
    
    for i in range(0, s):
        
        answer.append(my_list[i])
        
    b = list(reversed(my_list[s:e+1]))
    c = my_list[e+1:]
    
    for i in b:
        
        answer.append(i)
        
    for i in c:
        
        answer.append(i)
    
    return ''.join(answer)
