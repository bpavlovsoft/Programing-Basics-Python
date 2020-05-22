age = int(input())
price_washing_mashine = float(input())
toy_price = int(input())
number_toys = 0
saved_money = 0
money_birthday = 10
for i in range(1, age + 1):
    if i % 2 == 0:
        saved_money += (money_birthday - 1)
        money_birthday += 10
    else:
        number_toys += 1
saved_money += number_toys * toy_price
if saved_money >= price_washing_mashine:
    print('Yes! %.2f' % (saved_money - price_washing_mashine))
else:
    print('No! %.2f' % (price_washing_mashine - saved_money))    


