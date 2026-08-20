# 2026.08.20
# programmers188.py

def solution(binomial):
    
    num_list = binomial.split()
    answer = 0
    
    if num_list[1] == "+":
        
        answer =  int(num_list[0]) + int(num_list[2])
        
    elif num_list[1] == "-":
        
        answer =  int(num_list[0]) - int(num_list[2])
        
    elif num_list[1] == "*":
        
        answer =  int(num_list[0]) * int(num_list[2])
    
    return answer
