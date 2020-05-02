import math
numberOfHolidays = int(input())
playsInHolidays = numberOfHolidays * 127
playsInWorkDays = (365 - numberOfHolidays) * 63
totalPlays = playsInHolidays + playsInWorkDays
result = abs(30000 - totalPlays)
hours = result / 60
minutes = result % 60
if totalPlays < 30000:

    print('Tom sleeps well')
    print('{0} hours and {1} minutes less for play'.format(math.trunc(hours), minutes))
else:
    print('Tom will run away')
    print('{0} hours and {1} minutes more for play'.format(math.trunc(hours), minutes))