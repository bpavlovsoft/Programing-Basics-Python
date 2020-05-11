degrees = int(input())
daynight = input().lower()
if daynight == "morning":
    if 10 <= degrees and degrees <= 18:
        print(f"It's {degrees} degrees, get your Sweatshirt and Sneakers.")
    elif 18 < degrees and degrees <= 24:
        print(f"It's {degrees} degrees, get your Shirt and Moccasins.")
    elif degrees >= 25:
        print(f"It's {degrees} degrees, get your T-Shirt and Sandals.")
elif daynight == "afternoon":
    if 10 <= degrees and degrees <= 18:
        print(f"It's {degrees} degrees, get your Shirt and Moccasins.")
    elif 18 < degrees and degrees <= 24:
        print(f"It's {degrees} degrees, get your T-Shirt and Sandals.")
    elif degrees >= 25:
        print(f"It's {degrees} degrees, get your Swim Suit and Barefoot.")
elif daynight == "evening":
    if 10 <= degrees and degrees <= 18:
        print(f"It's {degrees} degrees, get your Shirt and Moccasins.")
    elif 18 < degrees and degrees <= 24:
        print(f"It's {degrees} degrees, get your Shirt and Moccasins.")
    elif degrees >= 25:
        print(f"It's {degrees} degrees, get your Shirt and Moccasins.")