year = int(input("Please Enter the Year Number you wish: "))

if  (( year%4 == 0 ) and ( year%100 != 0))):
    print("It is a Leap Year" %year)
else:
    print("It is Not the Leap Year" %year)
