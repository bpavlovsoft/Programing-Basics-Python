hour = int(input())
day = input().lower()
if hour >= 10 and hour <= 18:
    if day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday":
        print('open')
    elif day == "saturday" or day == "sunday":
        print('closed')
else:
    print('closed')