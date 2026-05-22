# 2026.05.22
# programmers63.py

def solution(my_string):
    
    arr = my_string.split()
    
    result = int(arr[0])
    
    for i in range(1,len(arr), 2):
        
        op = arr[i]
        num = int(arr[i + 1])
        
        if op == "+":
            
            result += num
            
        else:
            
            result -= num

    return result


# 좀 너무 어렵게 생각했음...
# 공백은 그냥 제거 대상으로만 보고 구분자로써 생각을 아예 안함
# 그리고 연산을 A + B 딱 이 형식으로만 생각해서
# A + B - C 이런식으로 후속으로 연산이 있을거라고 생각을 아예 안함
# ㅠㅠ
