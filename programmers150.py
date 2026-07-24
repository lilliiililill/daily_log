# 2026.07.24
# programmers150.py

def solution(q, r, code):
    
    code_list = list(code)
    answer = []
    
    for index, value in enumerate(code_list):
        
        if index % q == r:
            
            answer.append(code_list[index])
    
    return ''.join(answer)
