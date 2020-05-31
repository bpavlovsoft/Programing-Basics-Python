name = input()
counter = 1
grade = 0.0
while counter <= 12:
    graduates = float(input())
    if graduates >= 4:
        grade += graduates
    else:
        print(f'{name} has been excluded at {counter} grade')
        break        
    counter += 1
if counter >= 12:
    average = grade / 12
    print(f'{name} graduated. Average grade: {average:.2f}')    