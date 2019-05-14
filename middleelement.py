str1=input()
if (len(str1%3==0):
    m=len(str1)//3
    print(str1[:m-1]+'*'+'*'+str1[m+1:])
else:
    m=len(str1)//3
    print(str1[:m]+'*'+str1[m+1:])
