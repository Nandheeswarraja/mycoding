def checkDigits(n): 
    while (n>0):  
        # if digit is odd 
        if ((n % 10) % 2):  
            return False; 
        n =int(n/10); 
    return True; 
def evenNumber(n): 
    for i in range(n,-1,-1): 
        if (checkDigits(i)): 
            return i; 
a = 23;  
print(evenNumber(a)); 
