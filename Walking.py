goal = 10000;
sum = 0;
lastSteps = False;
 
while True:
    steps = input()
    if (steps == "Going home"):
        lastSteps = True
        continue
    num = int(steps);
    sum += num;
    if(sum >= goal or lastSteps):
        break
if sum >= goal:
    print("Goal reached! Good job!")
    print(f'{sum - goal} steps over the goal!')
else:
     print(f"{goal - sum} more steps to reach goal.")

