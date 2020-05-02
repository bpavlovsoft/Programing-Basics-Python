length = int(input())
width = int(input())
height = int(input())
percent = float(input())
volume = length * width * height
liters_water = volume * 0.001
total_percent = percent * 0.01
total_liters = liters_water * (1 - total_percent)
print(total_liters)