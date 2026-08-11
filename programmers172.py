# 2026.08.11
# programmers172.py

def solution(arr):
    
    answer = []
    count = 0
    
    while answer != arr:
        
        answer = arr
        arr = []
        
        for i in answer:
        
            if i >= 50 and i % 2 == 0:
            
                arr.append(i // 2)
            
            elif i < 50 and i % 2 != 0:
            
                arr.append(i * 2 + 1)
                      
            else:
            
                arr.append(i)
            
        count += 1
        
    return count - 1
