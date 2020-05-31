counter = 0
sum_amount = 0.0
while True:
    income = input()
    if income == "NoMoreMoney":
        break
    if float(income) < 0:
        print('Invalid operation!')
        break
    sum_amount += float(income)
    print(f'Increase: {float(income):.2f}')
print(f'Total: {sum_amount:.2f}')    

    
