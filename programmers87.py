# 2026.06.05
# programmers87.py

def solution(lines):
    
    count = {}
    
    for start, end in lines:
        
        for x in range(start, end): # 선분을 한칸씩 쪼갬
            
            count[x] = count.get(x, 0) + 1  # 딕셔너리에 각 구간을 카운팅 하는 방식
    
    answer = 0
    
    for v in count.values():
        
        if v >= 2:
            
            answer += 1
    
    return answer

# 위 처럼 풀면 차피 1칸 단위라 길이를 구 할때 그냥 다 더하면 끝남
