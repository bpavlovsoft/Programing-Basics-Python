import math
areaOfYard = int(input())
grapes = float(input())
litresWine = int(input())
workers = int(input())
totalGrapes = areaOfYard * grapes
wine = (totalGrapes * 0.40) / 2.5
diffWine = abs(wine - litresWine)
wineForWorkers = diffWine / workers
if wine > litresWine:
    print('Good harvest this year! Total wine: {0} liters.'.format(math.ceil(wine)))
    print('{0} liters left -> {1} liters per person.'.format(math.ceil(diffWine), math.ceil(wineForWorkers)))
else:
    print('It will be a tough winter! More {0} liters wine needed.'.format(math.floor(diffWine)))