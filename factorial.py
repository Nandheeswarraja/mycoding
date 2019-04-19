num=int(input("Enter a number"))
factorial=1
if(num<0):
  print("Sorry,factorial does not a negative number")
elif num==0:
  print("the factorial of o is 1":)
else:
  for i in range(1,num+1):
     factorial=factorial*i
  print("the factorial of",num,"is",factorial)
