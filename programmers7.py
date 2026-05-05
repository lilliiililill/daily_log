# 2026.05.05
# programmers7.py

from fractions import Fraction

def solution(numer1, denom1, numer2, denom2):
    answer = []
    
    f1 = Fraction(numer1, denom1)
    f2 = Fraction(numer2, denom2)
    
    result = f1 + f2
    
    answer.append(result.numerator)
    answer.append(result.denominator)
    
    return answer
