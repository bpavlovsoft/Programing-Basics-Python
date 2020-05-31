list1 = []
while True:
    command = input()
    if command == "Stop":
        break
    else:
        list1.append(command)
for i in range(0, len(list1)):
    print(list1[i])