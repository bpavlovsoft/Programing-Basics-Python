import math
record = float(input())
meters = float(input())
seconds = float(input())
total_seconds = meters * seconds
discount = (math.floor(meters / 15)) * 12.5
total_time = total_seconds + discount
if total_time > record:
    print('No, he failed! He was {:.2f} seconds slower.' .format(total_time - record))
else:
    print('Yes, he succeeded! The new world record is {:.2f} seconds.'.format(total_time))