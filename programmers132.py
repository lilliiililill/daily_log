# 2026.07.14
# programmers132.py

def solution(l, r):
    
    answer = []
    
    for number in range(l, r+1):
        
        if all(digit in "05" for digit in str(number)): # 이게 for문에서 추출한 요소를 문자형으로 바꾸고 바꾼 요소들을 각각 체크 해 0과 5만 있는지 확인함
            
            answer.append(number)
    
    return answer if answer else [-1]
