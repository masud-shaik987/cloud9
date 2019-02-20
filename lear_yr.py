y = int(input("Pleae enter a year:"))

if (y%4==0 and y%100!=0 or y%400==0):
    print("The year is {} is leap year".format(y))
else:
    print("Its not a leap year")
