n = int(input())
sum_even = 0
sum_odd = 0
for i in range(0, n):
    number = int(input())
    if i % 2 == 0:
        sum_even += number
    elif i % 2 != 0:
        sum_odd += number
if sum_even == sum_odd:
    print('Yes')
    print(f'Sum = {sum_even}')
else:
    print('No')
    print(f'Diff = {abs(sum_even - sum_odd)}')                