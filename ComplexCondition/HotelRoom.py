month = input()
nights = int(input())
total_cost_studio = 0
total_cost_apartmrnt = 0
total = 0
discount = 0
if month == "May" or month == "October":
    if nights > 7 and nights <= 14:
        total_cost_studio = (nights * 50) * 0.95
        total_cost_apartmrnt = nights * 65
        print(f'Apartment:{total_cost_apartmrnt: .2f} lv.')
        print(f'Studio:{total_cost_studio: .2f} lv.')
    elif nights > 14:
        total_cost_studio = (nights * 50) * 0.70
        total_cost_apartmrnt = (nights * 65) * 0.90
        print(f'Apartment:{total_cost_apartmrnt: .2f} lv.')
        print(f'Studio:{total_cost_studio: .2f} lv.')
elif month == "June" or month == "September":
    if nights > 7 and nights <= 14:
        total_cost_studio = nights * 75.20
        total_cost_apartmrnt = nights * 68.70
        print(f'Apartment:{total_cost_apartmrnt: .2f} lv.')
        print(f'Studio:{total_cost_studio: .2f} lv.')
    elif nights > 14:
        total_cost_studio = (nights * 75.20) * 0.80
        total_cost_apartmrnt = (nights * 68.70) * 0.90
        print(f'Apartment:{total_cost_apartmrnt: .2f} lv.')
        print(f'Studio:{total_cost_studio: .2f} lv.')
elif month == "July" or month == "August":
    if nights > 7 and nights <= 14:
        total_cost_studio = nights * 76
        total_cost_apartmrnt = nights * 77
        print(f'Apartment:{total_cost_apartmrnt: .2f} lv.')
        print(f'Studio: {total_cost_studio: .2f} lv.')
    elif nights > 14:
        total_cost_studio = nights * 76
        total_cost_apartmrnt = (nights * 77) * 0.90
        print(f'Apartment:{total_cost_apartmrnt: .2f} lv.')
        print(f'Studio:{total_cost_studio: .2f} lv.')