number = int(input('How many numbers: '))
total_sum = 0
for n in range(number):
    numbers = float(input('Enter number : '))
    total_sum += numbers
avg = total_sum/number
print('Average of ', number, ' numbers is :', avg)
