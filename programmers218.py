# 2026.09.08
# programmers218.py

def solution(arr, k):
    
    answer = []
    
    for i in arr:
        
        if k % 2 != 0:
            
            answer.append(i * k)
            
        else:
            
            answer.append(i + k)
    
    return answer
