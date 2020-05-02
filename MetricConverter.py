size = float(input())
sourceMetric = input().lower()
destMetric = input().lower()
if sourceMetric == "km":
    size = size / 0.001
elif sourceMetric == "mm":
    size = size / 1000
elif sourceMetric == "cm":
    size = size / 100
elif sourceMetric == "mi":
    size = size / 0.000621371192
elif sourceMetric == "in":
    size = size / 39.3700787
elif sourceMetric == "ft":
    size = size / 3.2808399
elif sourceMetric == "yd":
    size = size / 1.0936133
if destMetric == "ft":
    size = size * 3.2808399
elif destMetric == "km":
    size = size * 0.001
elif destMetric == "mm":
    size = size * 1000
elif destMetric == "cm":
    size = size * 100
elif destMetric == "in":
    size = size * 39.3700787
elif destMetric == "yd":
    size = size * 1.0936133
print('%.3f' % size)