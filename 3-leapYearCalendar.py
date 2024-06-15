year = int(input('Please input a year: '))

if (year % 100 == 0 and year % 400 == 0):
    print(year, 'is a leap year!')
elif (year % 100 != 0 and year % 4 == 0):
    print(year, 'is a leap year!')
else:
    print(year, 'is not a leap year.')