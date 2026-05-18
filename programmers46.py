# 2026.05.18
# programmers46.py

import re

def solution(my_string):
    
    result = re.sub(r'[^0-9]', '', my_string)
    result = list(map(int, result))
    
    result.sort()
    
    return result
