# 2026.08.27
# programmers198.py

def solution(strArr):
    
    count = [0] * 31
    
    for s in strArr:
        
        count[len(s)] += 1
        
        
    return max(count)
