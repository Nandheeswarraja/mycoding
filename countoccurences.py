def countOccurrences (e, d): 
    n = len(s) 
    c1 = 0
    c2 = 0
    C = 0
    for i in range(n): 
        if e[i] == 'a': 
            c1+= 1 
        if e[i] == 'b': 
            c2+= 1  
            C += c1   
    return C * d + (d * (d - 1) / 2) * c1 * c2 
e= "abcb"
d = 2
print (countOccurrences(S, k)) 
