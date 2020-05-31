width = int(input())
height = int(input())
cake = width * height
total = 0
while True:
    pieces = input()
    if pieces == "STOP":
        break
    total += int(pieces)
    if total > cake:
        break
if total > cake:
    print(f'No more cake left! You need {total - cake} pieces more.')
else:
    print(f'{cake - total} pieces are left.')            