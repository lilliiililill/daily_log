# 2026.05.12
# programmers31.py

def solution(emergency):
    
    emer_num = sorted(emergency, reverse = True)
    
    answer = [emer_num.index(s) + 1 for s in emergency]
    
    
    return answer
