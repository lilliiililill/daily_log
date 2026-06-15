# 2026.06.15
# programmers93.py

def solution(chicken):
    
    answer = 0
    coupon = chicken
    
    while coupon >= 10:
        
        service = coupon // 10  # 서비스로 나갈 치킨
        answer += service   # 최종적으로 나갈 치킨
        coupon = service + coupon % 10  # 서비스로 나갔던 치킨에서 생성된 쿠폰 + 남은 쿠폰
    
    return answer
