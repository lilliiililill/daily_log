# 2026.08.24
# programmers191.py

import re

def solution(myStr):
    
    answer = re.split("a|b|c", myStr)
    answer = [x for x in answer if x.strip()]
    
    if answer == []:
        
        answer.append("EMPTY")
        
        return answer
    
    else:
        
        return answer
    
    
