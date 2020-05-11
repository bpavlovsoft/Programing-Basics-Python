flowers= input()
count_flowers = int(input())
budget = int(input())
total_costs = 0
if flowers == "Roses":
    total_costs = count_flowers * 5
    if count_flowers > 80:
        discount_roses = total_costs * 0.10
        total_costs = total_costs - discount_roses
elif flowers == "Dahlias":
    total_costs = count_flowers * 3.80
    if count_flowers > 90:
        discount_roses = total_costs * 0.15
        total_costs = total_costs - discount_roses
elif flowers == "Tulips":
    total_costs = count_flowers * 2.80
    if count_flowers > 80:
        discount_roses = total_costs * 0.15
        total_costs = total_costs - discount_roses
elif flowers == "Narcissus":
    total_costs = count_flowers * 3
    if count_flowers < 120:
        discount_roses = total_costs * 0.15
        total_costs = total_costs + discount_roses
elif flowers == "Gladiolus":
    total_costs = count_flowers * 2.50
    if count_flowers < 80:
        discount_roses = total_costs * 0.20
        total_costs = total_costs + discount_roses
if total_costs > budget:
    print('Not enough money, you need %.2f leva more.' % (total_costs - budget))
else:
    difference = budget - total_costs
    print(f'Hey, you have a great garden with {count_flowers} {flowers} and {difference:.2f} leva left.')