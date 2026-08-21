# 2026.08.21
# programmers190.py

def solution(rny_string):
    
    rny_list = list(rny_string)
    answer = []
    
    for i in rny_list:
        
        if i == "m":
            
            answer.append("rn")
            
        else:
            
            answer.append(i)
    
    return "".join(answer)
