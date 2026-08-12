# 2026.08.12
# programmers175.py

def solution(myString, pat):
    
    answer = 0
    
    myString = myString.lower()
    pat = pat.lower()
    
    myString_list = list(myString)
    pat_list = list(pat)
    
    if len(pat_list) > len(myString_list):
        
        return 0
    
    else:
        
        for i in range(len(myString_list) - len(pat_list) + 1):
            
            if myString_list[i:i+len(pat_list)] == pat_list:
                
                return 1
            
        return 0
            
