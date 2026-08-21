# 2026.08.21
# programmers189.py

def solution(myString, pat):
    
    answer = 0
    
    myString = list(myString)
    str_list = []
    
    for i in myString:
        
        if i == "A":
            
            str_list.append("B")
            
        else:
            
            str_list.append("A")
            
    str_result = "".join(str_list)
    
    if pat in str_result:
        
        answer = 1
        
    else:
        
        answer = 0
    
    return answer
