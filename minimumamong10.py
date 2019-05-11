lst = []
n = int(input('How many numbers: '))
for i in range(n):
    num = int(input('Enter number '))
    lst.append(num)
print("\nMinimum element in the list is :", min(lst))
