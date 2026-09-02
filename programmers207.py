# 2026.09.02
# programmers207.py

def solution(a, b):
    
    i = len(a) - 1
    j = len(b) - 1
    carry = 0
    result = []
    
    while i >= 0 or j >= 0 or carry:
        
        x = int(a[i]) if i >= 0 else 0
        y = int(b[j]) if j >= 0 else 0
        
        total = x + y + carry
        
        result.append(str(total % 10))
        
        carry = total // 10
        
        i -= 1
        j -= 1
        
    return ''.join(reversed(result))
