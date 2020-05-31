amount = float(input())
amount = amount * 100
coin = 0
while amount > 0:
    if amount >= 200:
        coin += 1
        amount -= 200
    elif amount >= 100:
        coin += 1
        amount -= 100
    elif amount >= 50:
        coin += 1
        amount -= 50
    elif amount >= 20:
        coin += 1
        amount -= 20
    elif amount >= 10:
        coin += 1
        amount -= 10
    elif amount >= 5:
        coin += 1
        amount -= 5
    elif amount >= 2:
        coin += 1
        amount -= 2
    elif amount >= 1:
        coin += 1
        amount -= 1                        
print(coin)






