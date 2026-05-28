# 2026.05.28
# programmers74.py

def solution(my_str, n):
    
    answer = [my_str[i: i+n] for i in range(0, len(my_str), n)]
    
    return answer
