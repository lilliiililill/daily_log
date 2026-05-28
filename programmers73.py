# 2026.05.28
# programmers73.py

def solution(array):
    
    num_list = [int(digit) for n in array for digit in str(n)]
    
    answer = num_list.count(7)
    
    return answer
