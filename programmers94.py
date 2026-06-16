# 2026.06.16
# programmers94.py

def solution(bin1, bin2):
    
    answer = bin(int(bin1 ,2) + int(bin2, 2))[2:]
    
    return answer

# 2진수를 먼저 10진수로 변환 후 덧셈 연산 -> 10진수를 앞부분 0b 제거 후 2진수로 변환
