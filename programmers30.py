# 2026.05.12
# programmers30.py

def solution(age):
    
    age_list = list(map(int, str(age)))
    num_dic = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h", 8: "i", 9: "j"}
    
    result = [num_dic[item] for item in age_list if item in num_dic]
    
    answer = ''.join(result)
    
    return answer
