list1 = []
num = int(input())
for i in range (0, num):
    numbers = int(input())
    list1.append(numbers)
print(f'Max number: {max(list1)}')
print(f'Min number: {min(list1)}')    