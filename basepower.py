import math 
def Log2(a): 
    if a == 0: 
        return false;   
    return (math.log10(a) / 
            math.log10(2)); 
def isPowerOfTwo(n): 
    return (math.ceil(Log2(n)) == 
            math.floor(Log2(n))); 
if(isPowerOfTwo(31)): 
    print("Yes"); 
else: 
    print("No");   
if(isPowerOfTwo(64)): 
    print("Yes"); 
else: 
    print("No"); 
