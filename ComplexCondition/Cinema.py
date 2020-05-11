projection = input().lower()
rows = int(input())
colmuns = int(input())
income = 0
cinema = rows * colmuns
if projection == "premiere":
    income = cinema * 12.00
elif projection == "normal":
    income = cinema * 7.50
elif projection == "discount":
    income = cinema * 5.00
print('%.2f leva' % income)