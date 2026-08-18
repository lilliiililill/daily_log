# 2026.08.18
# programmers181.py

def solution(myString, pat):
    
    idx = myString.rfind(pat)
    
    return myString[:idx + len(pat)]
