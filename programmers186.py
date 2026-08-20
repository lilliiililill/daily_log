# 2026.08.20
# programmers186.py

def solution(myString):
    
    str_list = list(myString)
    count = 0
    answer = []
    
    for i in str_list:
        
        if i == "x":
            
            answer.append(count)
            count = 0
            
        else:
            
            count += 1
            
    answer.append(count)
    
    return answer
