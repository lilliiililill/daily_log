# 2026.06.19
# programmers97.py

def solution(A, B):
    
    for i in range(len(A)): # 문자열 길이만큼만 돌아봄
        
        if A == B:
            
            return i    # 돌아본 횟수 카운트
        
        A = A[-1] + A[:-1]  # 반복문 수행으로 인해 오른쪽으로 한칸씩 밈
    
    return -1   # 매칭이 안될 때 -1
