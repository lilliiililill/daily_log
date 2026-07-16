# 2026.07.16
# programmers137.py

from collections import Counter

def solution(a, b, c, d):
    
    counts = Counter([a, b, c, d])
    numbers = list(counts.keys())
    
    if len(numbers) == 1:
        
        p = numbers[0]
        
        return 1111 * p
    
    if len(numbers) == 2:
        
        p, q = numbers
        
        if counts[p] == 3:
            
            return (10 * p + q) ** 2
        
        if counts[q] == 3:
            
            return (10 * q + p) ** 2
            
        return (p + q) * abs(p - q)
    
    if len(numbers) == 3:
        
        different_numbers = [
            
            number for number in numbers
            if counts[number] == 1
            
        ]
        
        return different_numbers[0] * different_numbers[1]
    
    return min(numbers)
