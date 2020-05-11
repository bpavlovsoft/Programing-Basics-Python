budget = int(input())
season = input()
count_fisherman = int(input())
rent_boat = 0.0
discount = 0.0
total_costs = 0
if season == "Spring":
    rent_boat = 3000
elif season == "Summer":
    rent_boat = 4200
elif season == "Autumn":
    rent_boat = 4200
elif season == "Winter":
    rent_boat = 2600
if count_fisherman <= 6:
    total_costs = rent_boat - (rent_boat * 0.10)
elif count_fisherman > 7 and count_fisherman <= 11:
    total_costs = rent_boat - (rent_boat * 0.15)
elif count_fisherman > 12:
    total_costs = rent_boat - (rent_boat * 0.25)
if (count_fisherman % 2 == 0 and season != "Autumn"):
    total_costs = total_costs * 0.95
result = budget - total_costs
if result >= 0:
    print('Yes! You have %.2f leva left.' % result)
else:
    print('Not enough money! You need %.2f leva.' % -result)