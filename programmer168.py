# 2026.08.07
# programmer168.py

def solution(todo_list, finished):
    
    answer = []
    
    for x, y in zip(todo_list, finished):
        
        if y == False:
            
            answer.append(x)
    
    return answer
