needed_money = float(input())
owned_money = float(input())
count_days = 0
count_spend = 0
while owned_money < needed_money and count_spend < 5:
    command = input()
    money = float(input())
    count_days += 1
    if command == "save":
        owned_money += money
        count_spend = 0
    elif command == "spend":
        owned_money -= money
        count_spend += 1
        if owned_money < 0:
            owned_money = 0
if count_spend == 5:
    print('You can\'t save the money.')
    print(count_days)
if owned_money >= needed_money:
    print(f'You saved the money for {count_days} days.')                    