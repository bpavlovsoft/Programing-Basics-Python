budget = float(input())
statists = int(input())
price_clothes = float(input())
decor = budget * 0.10
amount_clothes = statists * price_clothes
total_budget = 0
discount_clothes = 0
if statists > 150:
    discount_clothes = amount_clothes * 0.10
    amount_clothes = amount_clothes - discount_clothes
    total_budget = decor + amount_clothes
    if total_budget < budget:
        print('Action!')
        print('Wingard starts filming with %.2f leva left.' % (budget - total_budget))
    else:
        print('Not enough money!')
        print('Wingard needs %.2f leva more.' % (total_budget - budget))
else:
    total_budget = decor + amount_clothes
    if total_budget < budget:
        print('Action!')
        print('Wingard starts filming with %.2f leva left.' % (budget - total_budget))
    else:
        print('Not enough money!')
        print('Wingard needs %.2f leva more.' % (total_budget - budget))
