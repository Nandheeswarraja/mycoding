def round(num): 
    a = (num// 10) * 10
    b = a + 10
    return (b if num - a > b - num else a)  
num=4722
print(round(num)) 
  
