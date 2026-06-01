# 2026.06.01
# programmers84.py

def solution(spell, dic):
    
    for word in dic:
        
        if sorted(word) == sorted(spell):
            
            return 1
        
    return 2
