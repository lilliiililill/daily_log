# 2026.06.10
# programmers90.py

def solution(score):
    
    averages = [sum(s) / 2 for s in score]  # 평균을 구한 리스트
    answer = []
    
    for avg in averages:    # 평균 값들을 하나씩 꺼냄
        
        rank = 1    # 초기 등수를 1로 책정
        
        for other in averages:  # 현시점 평균값과 비교를 위한 반복문 수행
            
            if other > avg: # 현재 값보다 다른 평균값이 크다면
                
                rank += 1   # 등수를 1씩 증가 // 이렇게 하면 현재보다 큰 평균의 개수만큼 등수가 밀림 그래서 조건에 부합함
                
        answer.append(rank) # 결과 리스트에 등수 저장
    
    return answer
