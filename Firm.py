import math
hoursNeeded = int(input())
daysForProject = int(input())
workers = int(input())
learnDays = daysForProject * 0.10
totalHours = (daysForProject - learnDays) * 8
totalExtraHours = workers * (2 * daysForProject)
total = math.floor(totalHours + totalExtraHours)
difference = abs(total - hoursNeeded)
if total > hoursNeeded:
    print('Yes!{0} hours left.'.format(difference))
else:
    print('Not enough time!{0} hours needed.'.format(difference))
