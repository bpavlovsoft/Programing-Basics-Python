length_room = int(input())
width_room = int(input())
height_room = int(input())
volume_room = length_room * width_room * height_room
total_boxes = 0
while True:
    volume_boxes = input()
    if volume_boxes == "Done":
        print(f'{volume_room - total_boxes} Cubic meters left.')
        break
    total_boxes += int(volume_boxes)
    if total_boxes > volume_room:
        print(f'No more free space! You need {total_boxes - volume_room} Cubic meters more.')
        break
     