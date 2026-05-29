# 2026.05.29
# programmers79.py

def solution(numbers):
    
    numbers.sort()
    
    case1 = numbers[0] * numbers[1]
    case2 = numbers[-1] * numbers[-2]
    
    answer = max(case1, case2)
    
    return answer
