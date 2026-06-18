# 2026.06.18
# programmers96.py

def solution(i, j, k):
    
    answer = 0
    
    for a in range(i, j+1):
        
        a_list = list(map(int, str(a)))
        
        for x in a_list:
            
            if x == k:
                
                answer += 1
    
    return answer
