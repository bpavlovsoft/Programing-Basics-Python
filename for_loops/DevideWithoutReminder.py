list1 = []
n = int(input())
count2 = 0
histo2 = 0.0
count3 = 0
histo3 = 0.0
count4 = 0
histo4 = 0.0
for i in range(1, n + 1):
    number = int(input())
    list1.append(number)
for i in range(0, len(list1)):
    if list1[i] % 2 == 0:
        count2 += 1
        histo2 = (count2 / len(list1)) * 100
    if list1[i] % 3 == 0:
        count3 += 1
        histo3 = (count3 / len(list1)) * 100
    if list1[i] % 4 == 0:
        count4 += 1
        histo4 = (count4 / len(list1)) * 100
print(f'{histo2:.2f}%')        
print(f'{histo3:.2f}%')
print(f'{histo4:.2f}%')                