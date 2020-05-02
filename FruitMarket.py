price_of_berries = float(input())
quantity_banana = float(input())
quantity_orange = float(input())
quantity_raspberries = float(input())
quantity_berries = float(input())
price_raspberries = price_of_berries / 2
price_orange = price_raspberries - (price_raspberries * 0.40)
price_banan = price_raspberries - (price_raspberries * 0.80)
total_banana = price_banan * quantity_banana
total_orange = price_orange * quantity_orange
total_raspberrie = price_raspberries * quantity_raspberries
total = (price_of_berries * quantity_berries) + total_banana + total_orange + total_raspberrie
print(total)