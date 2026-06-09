# 2026.06.09
# programmers89.py

def solution(numlist, n):
    
    return sorted(numlist, key = lambda x: (abs(x - n), -x))

# 튜플 형태로 지정한 n과의 차이가 가장 작고 차이가 똑같다면 큰 수를 앞으로 오게 만들어서 정렬
