days = int(input())
room = input().lower()
rate = input().lower()
nights = days - 1
total_price = 0
discount = 0
if room == "room for one person":
    if nights <= 10:
        total_price = nights * 18.00
        if rate == "positive":
            total_price = total_price + (total_price * 0.25)
            print('%.2f' % total_price)
        elif rate == "negative":
            total_price = total_price - (total_price * 0.10)
            print('%.2f' % total_price)
    elif 10 < nights and nights <= 15:
        total_price = nights * 18.00
        if rate == "positive":
            total_price = total_price + (total_price * 0.25)
            print('%.2f' % total_price)
        elif rate == "negative":
            total_price = total_price - (total_price * 0.10)
            print('%.2f' % total_price)
    elif nights > 15:
        total_price = nights * 18.00
        if rate == "positive":
            total_price = total_price + (total_price * 0.25)
            print('%.2f' % total_price)
        elif rate == "negative":
            total_price = total_price - (total_price * 0.10)
            print('%.2f' % total_price)
elif room == "apartment":
    if nights <= 10:
        total_price = (nights * 25.00)
        discount = total_price * 0.30
        total_price = total_price - discount
        if rate == "positive":
            total_price = total_price + (total_price * 0.25)
            print('%.2f' % total_price)
        elif rate == "negative":
            total_price = total_price - (total_price * 0.10)
            print('%.2f' % total_price)
    elif 10 < nights and nights <= 15:
        total_price = nights * 25.00
        discount = total_price * 0.35
        total_price = total_price - discount
        if rate == "positive":
            total_price = total_price + (total_price * 0.25)
            print('%.2f' % total_price)
        elif rate == "negative":
            total_price = total_price - (total_price * 0.10)
            print('%.2f' % total_price)
    elif nights > 15:
        total_price = nights * 25.00
        discount = total_price * 0.50
        total_price = total_price - discount
        if rate == "positive":
            total_price = total_price + (total_price * 0.25)
            print('%.2f' % total_price)
        elif rate == "negative":
            total_price = total_price - (total_price * 0.10)
            print('%.2f' % total_price)
elif room == "president apartment":
    if nights <= 10:
        total_price = nights * 35.00
        discount = total_price * 0.10
        total_price = total_price - discount
        if rate == "positive":
            total_price = total_price + (total_price * 0.25)
            print('%.2f' % total_price)
        elif rate == "negative":
            total_price = total_price - (total_price * 0.10)
            print('%.2f' % total_price)
    elif 10 < nights and nights <= 15:
        total_price = nights * 35.00
        discount = total_price * 0.15
        total_price = total_price - discount
        if rate == "positive":
            total_price = total_price + (total_price * 0.25)
            print('%.2f' % total_price)
        elif rate == "negative":
            total_price = total_price - (total_price * 0.10)
            print('%.2f' % total_price)
    elif nights > 15:
        total_price = nights * 35.00
        discount = total_price * 0.20
        total_price = total_price - discount
        if rate == "positive":
            total_price = total_price + (total_price * 0.25)
            print('%.2f' % total_price)
        elif rate == "negative":
            total_price = total_price - (total_price * 0.10)
            print('%.2f' % total_price)