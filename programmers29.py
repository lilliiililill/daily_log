# 2026.05.12
# programmers29.py

def solution(numbers, num1, num2):
    
    answer = []
    
    for i in numbers[num1: num2+1]:
        
        answer.append(i)
    
    return answer
