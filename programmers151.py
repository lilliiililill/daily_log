# 2026.07.27
# programmers151.py

def solution(my_string):
    
    answer = [0] * 52
    
    for char in my_string:
        
        if char.isupper():
            
            index = ord(char) - ord('A')
            
        else:
            
            index = ord(char) - ord('a') + 26
            
        answer[index] += 1
    
    return answer
