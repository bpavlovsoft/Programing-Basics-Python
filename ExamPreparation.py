failed_evaluation = int(input())
failed_times = 0
count_solves = 0
total_grade = 0
last_problem = ''
has_failed = True
while failed_times < failed_evaluation:
    problem_name = input()
    if problem_name == "Enough":
        has_failed = False
        break
    grade = int(input())
    if grade <= 4:
        failed_times += 1
    total_grade += grade
    count_solves += 1
    last_problem = problem_name
if has_failed:
    print(f'You need a break, {failed_evaluation} poor grades.') 
else:
    print(f'Average score: {total_grade / count_solves:.2f}')
    print(f'Number of problems: {count_solves}')
    print(f'Last problem: {last_problem}')           
