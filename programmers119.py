# 2026.07.07
# programmers119.py

def solution(ineq, eq, n, m):
    
    answer = 0
    
    if ineq == ">" and eq == "=":
        
        answer = int(n >= m)
        
    elif ineq == "<" and eq == "=":
        
        answer = int(n <= m)
        
    elif ineq == ">" and eq == "!":
        
        answer = int(n > m)
        
    elif ineq == "<" and eq == "!":
        
        answer = int(n < m)
        
    return answer
