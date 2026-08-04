# 2026.08.04
# programmers163.py

def solution(str_list):
    
    answer = []
    
    for i in str_list:
        
        if i == "l" or i == "r":
            
            if i == "l":
                
                idx_l = str_list.index('l')
                
                for j in str_list[:idx_l]:
                    
                    answer.append(j)
                    
                break
                
                
            elif i == "r":
                
                idx_r = str_list.index('r')
                
                for x in str_list[idx_r+1:]:
                    
                    answer.append(x)
                    
                break

    return answer
