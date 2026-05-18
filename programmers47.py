# 2026.05.18
# programmers47.py

import re

def solution(my_string):
    
    result = re.sub(r'[^0-9]', '', my_string)
    result = list(map(int, result))
    
    return sum(result)
