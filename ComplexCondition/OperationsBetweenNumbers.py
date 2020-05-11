number1 = int(input())
number2 = int(input())
operation = input()
result = 0
if operation == "+":
    result = number1 + number2
    if result % 2 == 0:
        print(f'{number1} + {number2} = {result} - even')
    elif result % 2 != 0:
        print(f'{number1} + {number2} = {result} - odd')
elif operation == "-":
    result = number1 - number2
    if result % 2 == 0:
        print(f'{number1} - {number2} = {result} - even')
    elif result % 2 != 0:
        print(f'{number1} - {number2} = {result} - odd')
elif operation == "*":
    result = number1 * number2
    if result % 2 == 0:
        print(f'{number1} * {number2} = {result} - even')
    elif result % 2 != 0:
        print(f'{number1} * {number2} = {result} - odd')
elif operation == "/":
    if number2 != 0:
        result = number1 / number2
        print(f'{number1} / {number2} ={result: .2f}')
    else:
        print(f'Cannot divide {number1} by zero')
elif operation == "%":
    if number2 != 0:
        result = number1 % number2
        print(f'{number1} % {number2} = {result}')
    else:
        print(f'Cannot divide {number1} by zero')