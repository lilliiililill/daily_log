# 2026.09.10
# programmers221.py

def solution(n):
    
    answer = [[0] * n for _ in range(n)]
    
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    
    r, c = 0, 0
    
    direction = 0
    
    for num in range(1, n * n + 1):
        
        answer[r][c] = num
        
        nr = r + dr[direction]
        nc = c + dc[direction]
        
        if (
        
            nr < 0 or nr >= n or
            nc < 0 or nc >= n or
            answer[nr][nc] != 0
        
        ):
            
            direction = (direction + 1) % 4
            
            nr = r + dr[direction]
            nc = c + dc[direction]
            
        r, c = nr, nc
    
    
    return answer
