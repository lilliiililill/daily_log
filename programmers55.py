# 2026.05.20
# programmers55.py

def solution(cipher, code):
    
    cipher_list = list(cipher)
    result = []
    
    for i in range(code-1, len(cipher_list), code):
        
        result.append(cipher_list[i])
    
    answer = ''.join(result)
    
    return answer
