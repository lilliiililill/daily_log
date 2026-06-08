# 2026.06.08
# programmers88.py

import math

def solution(a, b):
    
    x = math.gcd(a, b)  # 기약분수 만들땐 최대공약수를 써야해서 최대 공약수를 구함
    w = b // x  # 분자는 필요없고 분모를 최대공약수로 나눠서 기약분수 분모를 구함
    
    while w % 2 == 0:   # 2로 우선 나눌 수 있을 때 까지 나눔
        
        w //= 2
    
    while w % 5 == 0:   # 2로 나누고 더 못 나눌 때 5로 나눔
        
        w //= 5
        
    return 1 if w == 1 else 2   # 그러고 나서 남은 분모값이 최종적으로 1이면 유한, 아니면 무한으로 판단해 결과 출력
