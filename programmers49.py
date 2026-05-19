# 2026.05.19
# programmers49.py

def solution(s):
    
    s_list = s.split()
    
    answer = 0
    
    for i in range(0, len(s_list)):
        
        if s_list[i] == "Z":
            
            answer -= int(s_list[i-1])
            
        else:
            
            answer += int(s_list[i])
    
    return answer
