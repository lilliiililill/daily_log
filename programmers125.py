# 2026.07.09
# programmers125.py

def solution(num_list):
    
    even_list = []
    odd_list = []
    
    for i in num_list:
        
        if i % 2 == 1:
            
            odd_list.append(i)
            
        else:
            
            even_list.append(i)
            
    odd_num = int(''.join(map(str, odd_list)))
    even_num = int(''.join(map(str, even_list)))
    
    answer = odd_num + even_num
    
    return answer
