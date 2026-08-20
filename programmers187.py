# 2026.08.20
# programmers187.py

def solution(myString):
    
    answer = myString.split("x")
    answer = [x for x in answer if x.strip()]
    
    return sorted(answer)
