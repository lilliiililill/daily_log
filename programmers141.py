# 2026.07.21
# programmers141.py

def solution(intStrs, k, s, l):
    
    answer = []
    
    for i in intStrs:
        
        i = list(i)
        ess_num = i[s: s+l]
        ess_num = ''.join(ess_num)
        ess_num = int(ess_num)
        
        if ess_num > k:
            
            answer.append(ess_num)
    
    return answer
