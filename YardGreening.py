yard = float(input())
greening_yard = (yard * 7.61)
discount = greening_yard * 0.18
print('The final price is: {0} lv.'.format(greening_yard - discount))
print('The discount is: {0} lv.'.format(discount))