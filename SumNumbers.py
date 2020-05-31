n = int(input())
sum = 0
while sum < n:
    number = int(input())
    sum += number
    if sum >= n:
        print(sum)
        break 