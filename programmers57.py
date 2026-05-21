# 2026.05.21
# programmers57.py

def solution(numbers):
    
    words = {
        
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
        
    }
    
    answer = numbers
    
    for word, num in words.items():
        
        answer = answer.replace(word, num)
    
    return int(answer)

# replace 쓰면 문자열이 붙어 있어도 알아서 단어로 찾아서 매칭시켜서 값을 변화시킴
