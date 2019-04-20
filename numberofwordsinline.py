sentence=input("Enter a string :")
count=0
for c in sentence:
  if c.isspace() != True:
    count=count+1
  print("total number of character",count)
