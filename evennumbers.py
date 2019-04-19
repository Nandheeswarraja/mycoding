start=int(input("Enter a number"))
end=int(input("Enter a number"))
for num in range(start, end + 1):
    if num % 2 == 0:
        print(num, end = " ") 
