# 2026.06.04
# programmers86.py

def solution(dots):
    
    def parallel(a, b, c, d):
        
        return (b[1] - a[1]) * (d[0] - c[0]) == (d[1] - c[1]) * (b[0] - a[0])
    
    if parallel(dots[0], dots[1], dots[2], dots[3]):
        
        return 1
    
    if parallel(dots[0], dots[2], dots[1], dots[3]):
        
        return 1
    
    if parallel(dots[0], dots[3], dots[1], dots[2]):
        
        return 1
    
    return 0

"""

평행 = 기울기가 같다 => 위 문제 같은거에 중요한 포인트

앞으로 평행, 일직선, 직선, 좌표 이런 단어가 나올시 기울기를 먼저 떠올리면 좋음

"좌표 문제에서 "평행"이란 단어가 나오면 기울기를 이용한다 (포인트)

"""

