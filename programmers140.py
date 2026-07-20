# 2026.07.20
# programmers140.py

def solution(my_string, queries):
    
    my_list = list(my_string)
    
    for x, y in queries:
        
        my_list[x: y+1] = my_list[x: y+1][::-1] # 구간 부분을 자르고 자른 부분을 역으로 적용
        

    return "".join(my_list)
