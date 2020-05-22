import math
year = input()
holidays = int(input())
weekends = int(input())
weekend_in_year = 48
weekend_sofia = weekend_in_year - weekends
plays_in_sofia = weekend_sofia * 3 / 4
plays_in_holiday = holidays * 2 / 3
total_plays = plays_in_sofia + weekends + plays_in_holiday
if year == "leap":
    total_plays = total_plays + (total_plays * 0.15)
    print(math.floor(total_plays))
else:
    print(math.floor(total_plays))        