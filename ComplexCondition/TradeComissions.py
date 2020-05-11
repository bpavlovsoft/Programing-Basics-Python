town = input().lower()
sales = float(input())
commision = -1
if town == "sofia":
    if 0 <= sales and sales <= 500:
        commision = 0.05
    elif 500 < sales and sales <= 1000:
        commision = 0.07
    elif 1000 < sales and sales <= 10000:
        commision = 0.08
    elif sales > 10000:
        commision = 0.12
elif town == "varna":
    if 0 <= sales and sales <= 500:
        commision = 0.045
    elif 500 < sales and sales <= 1000:
        commision = 0.075
    elif 1000 < sales and sales <= 10000:
        commision = 0.10
    elif sales > 10000:
        commision = 0.13
elif town == "plovdiv":
    if 0 <= sales and sales <= 500:
        commision = 0.055
    elif 500 < sales and sales <= 1000:
        commision = 0.08
    elif 1000 < sales and sales <= 10000:
        commision = 0.12
    elif sales > 10000:
        commision = 0.145
if commision >= 0:
    print("%.2f" % (sales * commision))
else:
    print('error')