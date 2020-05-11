budget = float(input())
season = input()
total_cost = 0.0
if budget <= 100:
    print('Somewhere in Bulgaria')
    if season == "summer":
        total_cost = budget * 0.30
        print(f'Camp -{total_cost: .2f}')
    elif season == "winter":
         total_cost = budget * 0.70
         print(f'Hotel -{total_cost: .2f}')
elif budget <= 1000:
    print('Somewhere in Balkans')
    if season == "summer":
        total_cost = budget * 0.40
        print(f'Camp -{total_cost: .2f}')
    elif season == "winter":
        total_cost = budget * 0.80
        print(f'Hotel -{total_cost: .2f}')
elif budget > 1000:
    print('Somewhere in Europe')
    if season == "summer" or season == "winter":
        total_cost = budget * 0.90
        print(f'Hotel -{total_cost: .2f}')