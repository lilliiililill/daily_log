# 2026.07.02
# programmers111.py

def solution(str1, str2):
    
    answer = []
    
    for x, y in zip(str1, str2):
        
        answer.append(x+y)
    
    return ''.join(answer)
