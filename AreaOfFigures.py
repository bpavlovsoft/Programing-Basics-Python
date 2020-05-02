import math
figure = input().lower()
if figure == "square":
    side = float(input())
    area = side * side
    print('%.3f' % area)
elif figure == "rectangle":
    side1 = float(input())
    side2 = float(input())
    area = side1 * side2
    print('%.3f' % area)
elif figure == "circle":
     radius = float(input())
     area = math.pi * radius * radius
     print('%.3f' % area)
elif figure == "triangle":
    a = float(input())
    h = float(input())
    area = (a * h) / 2
    print('%.3f' % area)