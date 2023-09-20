def find_nb(m):
    
    
    total = 0
    a = 0
    
    while a < m:
        total += a + 1 **3
        
    return total if total == m else -1    

        


print(find_nb(4183059834009))