# 2026.07.20
# programmers139.py

def solution(number):
      
    n_list = list(map(int,(number)))
    
    answer = sum(n_list) % 9
    
    return answer
