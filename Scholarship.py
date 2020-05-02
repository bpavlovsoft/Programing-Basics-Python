incomes = float(input())
grade = float(input())
minimal_salary = float(input())
if incomes > minimal_salary:
    if grade < 5.50:
        print('You cannot get a scholarship!')
elif incomes < minimal_salary:
