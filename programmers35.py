# 2026.05.13
# programmers35.py

def solution(rsp):
    
    rsp_list = list(rsp)
    win_dic = {"2": "0", "0": "5", "5": "2"}
    
    result = [win_dic[item] for item in rsp_list if item in win_dic]
    
    answer = ''.join(result)
    
    return answer
