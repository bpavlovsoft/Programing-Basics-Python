amount = float(input())
time_of_deposit = int(input())
year_rate = float(input())
total_year_rate = amount * (year_rate / 100)
month_rate = total_year_rate / 12
result = amount + (time_of_deposit * month_rate)
print(result)
