list_new = []
n = int(input())
total = 0
max1 = 0
for i in range(1, n + 1):
    numbers = int(input())
    list_new.append(numbers)
for i in range(0, len(list_new)):
    total += list_new[i]
if max(list_new) == (total - max(list_new)):
    print('Yes')
    print(f'Sum = {max(list_new)}')
else:
    diff = abs(max(list_new) - (total - max(list_new)))
    print('No')
    print(f'Diff = {diff}')            
 
