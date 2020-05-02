trip = float(input())
puzzels = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())
total_puzzels = puzzels * 2.60
total_dolls = dolls * 3
total_bears = bears * 4.10
total_minions = minions * 8.20
total_trucks = trucks * 2
total_incomes = total_puzzels + total_dolls + total_bears + total_minions + total_trucks
count_toys = puzzels + dolls + bears + minions + trucks
rent = 0
earning = 0
if count_toys >= 50:
    total_incomes = total_incomes - (total_incomes * 0.25)
    rent = total_incomes * 0.10
    earning = total_incomes - rent
else:
    rent = total_incomes * 0.10
    earning = total_incomes - rent
if earning > trip:
    print('Yes! %.2f lv left.' % (earning - trip))
else:
    print('Not enough money! %.2f lv needed.' % (trip - earning))

