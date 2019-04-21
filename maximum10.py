lst = []
number = int(input('How many numbers: '))
for n in range(number):
    num = int(input('Enter number '))
    lst.append(num)
print("Maximum element in the list is :", max(lst), "\nMinimum element in the list is :", min(lst))
