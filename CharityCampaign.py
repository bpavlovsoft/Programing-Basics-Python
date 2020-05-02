days_of_campaign = int(input())
count_of_cookers = int(input())
count_of_sweets = int(input())
count_of_gofrets = int(input())
count_of_pancakes = int(input())
money_one_cookers = (count_of_sweets * 45) + (count_of_gofrets * 5.80) + (count_of_pancakes * 3.20)
total_money = money_one_cookers * count_of_cookers
total = total_money * days_of_campaign
result = total - total / 8
print(result)