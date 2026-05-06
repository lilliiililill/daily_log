# 2026.05.06
# programmers11.py

from collections import Counter

def solution(array):
    
    counter = Counter(array)
    max_freq = max(counter.values())
    
    answer = [k for k, v in counter.items() if v == max_freq]
    
    return answer[0] if len(answer) == 1 else -1
