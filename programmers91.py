# 2026.06.11
# programmers91.py

def solution(babbling):
    
    answer = 0
    sounds = ["aya", "ye", "woo", "ma"]
    
    for word in babbling:
        
        for sound in sounds:
            
            word = word.replace(sound, " ")
            
        # 위 방식은 발음 가능한 단어와 일치하면 공백으로 치환
            
        if word.strip() == "":
            
            answer += 1
            
        # 그리고 전체적으로 아예 안남게 된다면 카운트 +1
    
    return answer
