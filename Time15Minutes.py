hours = int(input())
minutes = int(input())
after15Minutes = minutes + 15
if after15Minutes > 59:
    hours = hours + 1
    after15Minutes = abs(after15Minutes - 60)
if hours > 23:
    hours = hours - 24
if after15Minutes < 10:
    print(f'{hours}:0{after15Minutes}')
else:
    print(f'{hours}:{after15Minutes}')
