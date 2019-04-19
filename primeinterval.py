start = int(input("Enter a number"))
end = int(input("Enter a number"))
for val in range(start, end ):
  if val > 1:
    for n in range(2,val):
      if (val % n) == 0:
        break
      else:
        print(val) 
