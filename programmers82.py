# 2026.06.01
# programmers82.py

def solution(board):
    
    n = len(board)
    
    danger = [row[:] for row in board]
    
    directions = [
        
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1), (1, 0),   (1, 1)
                
    ]
    
    for i in range(n):
        
        for j in range(n):
            
            if board[i][j] == 1:
                
                for dx, dy in directions:
                    
                    nx = i + dx
                    ny = j + dy
                    
                    if 0 <= nx < n and 0 <= ny < n:
                        
                        danger[nx][ny] = 1
    
    answer = 0
    
    for row in danger:
        
        answer += row.count(0)
        
    return answer
