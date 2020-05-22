list1 = []
n = int(input())
histo1 = 0.0
count1 = 0
histo2 = 0.0
count2 = 0
histo3 = 0.0
count3 = 0
count4 = 0
histo4 = 0.0
count5 = 0
histo5 = 0.0
for i in range(1, n + 1):
    number = int(input())
    list1.append(number)
for i in range(0, len(list1)):
    if list1[i] < 200:
        count1 += 1
        histo1 = (count1 / len(list1)) * 100
    elif list1[i] >= 200 and list1[i] <= 399:
        count2 += 1
        histo2 = (count2 / len(list1)) * 100
    elif  list1[i] >= 400 and list1[i] <= 599:
        count3 += 1
        histo3 = (count3 / len(list1)) * 100
    elif list1[i] >= 600 and list1[i] <= 799:
        count4 += 1
        histo4 = (count4 / len(list1)) * 100
    elif list1[i] >= 800:
        count5 += 1
        histo5 = (count5 / len(list1)) * 100
print(f'{histo1:.2f}%')
print(f'{histo2:.2f}%')
print(f'{histo3:.2f}%')
print(f'{histo4:.2f}%')
print(f'{histo5:.2f}%')
