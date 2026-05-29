# 2026.05.29
# programmers80.py

def solution(polynomial):
    
    x_sum = 0
    num_sum = 0
    
    terms = polynomial.split(" + ")
    
    for term in terms:
        
        if "x" in term:
            
            if term == "x":
                
                x_sum += 1
                
            else:
                
                x_sum += int(term[:-1])
                
        else:
            
            num_sum += int(term)
            
    if x_sum == 0:
        
        return str(num_sum)
    
    elif num_sum == 0:
    
        if x_sum == 1:
            
            return "x"
        
        return str(x_sum) + "x"
    
    else:
        
        if x_sum == 1:
            
            return "x + " + str(num_sum)
        
        return str(x_sum) + "x + " + str(num_sum)
