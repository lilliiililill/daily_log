# 2026.05.21
# programmers59.py

def solution(s):
    
    one_chars = [char for char in s if s.count(char) == 1]
    
    one_chars.sort()
    
    answer = ''.join(one_chars)
    return answer
