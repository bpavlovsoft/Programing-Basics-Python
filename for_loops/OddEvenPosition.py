import sys
n = int(input())
sum_even = 0
max_even = -sys.maxsize
min_even = sys.maxsize 
sum_odd = 0
max_odd = -sys.maxsize
min_odd = sys.maxsize
minimum = float('inf')
maximum = float('-inf')
for i in range(1, n + 1):
    numbers = float(input())
    if i % 2 == 0:
        sum_even += numbers
        if numbers < min_even:
            min_even = numbers
        if numbers > max_even:
            max_even = numbers
    elif i % 2 != 0:
        sum_odd += numbers
        if numbers < min_odd:
            min_odd = numbers
        if numbers > max_odd:
            max_odd = numbers
print(f'OddSum={sum_odd:.2f},')
if min_odd == sys.maxsize:
    print('OddMin=No,')
else:
    print(f'OddMin={min_odd:.2f},')
if max_odd == -sys.maxsize:
    print('OddMax=No,')
else: 
    print(f'OddMax={max_odd:.2f},')
print(f'EvenSum={sum_even:.2f},')        
if min_even == sys.maxsize:
    print('EvenMin=No,')
else:
    print(f'EvenMin={min_even:.2f},')
if max_even == -sys.maxsize:
    print('EvenMax=No')
else: 
    print(f'EvenMax={max_even:.2f}')        
                     