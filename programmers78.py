# 2026.05.29
# programmers78.py

def solution(keyinput, board):
    
    x = 0
    y = 0
    
    x_limit = board[0] // 2
    y_limit = board[1] // 2
    
    for key in keyinput:
        
        if key == "left":
            
            if x > -x_limit:
                
                x -= 1
                
        elif key == "right":
            
            if x < x_limit:
                
                x += 1
        
        elif key == "up":
            
            if y < y_limit:
                
                y += 1
                
        elif key == "down":
        
            if y > -y_limit:
                
                y -= 1
                

    return [x, y]
