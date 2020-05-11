month = input()
nights = int(input())
discount_studio = 0
discount_apartment = 0
price_studio = 0
price_apartment = 0
total_cost_studio = -1
total_cost_apartment = -1
if month == "May" or month == "October":
    price_studio = 50
    price_apartment = 65
    if nights > 7 and nights <= 14:
        discount_studio = 0.05
        discount_apartment = 0
        total_cost_studio = (nights * price_studio) - (price_studio * discount_studio)
        total_cost_apartment = (nights * price_apartment) - (price_apartment * discount_apartment)
    elif nights > 14:
        discount_studio = 0.30
        discount_apartment = 0.10
elif month == "June" or month == "September":
    price_studio = 75.20
    price_apartment = 68.70
    if nights > 7 and nights <= 14:
        discount_studio = 0
        discount_apartment = 0
    elif nights > 14:
        discount_studio = 0.20
        discount_apartment = 0.10
elif month == "July" or month == "August":
    price_studio = 76
    price_apartment = 77
    if nights > 7 and nights <= 14:
        discount_studio = 0
        discount_apartment = 0
    elif nights > 14:
        discount_apartment = 0.10
        discount_studio = 0
if total_cost_studio >= 0 and total_cost_apartment >= 0:
   total_cost_studio = (nights * price_studio) - (price_studio * discount_studio)
   total_cost_apartment = (nights * price_apartment) - (price_apartment * discount_apartment)
   print(f'Apartment:{total_cost_apartment: .2f} lv.')
   print(f'Studio:{total_cost_studio: .2f} lv.')
