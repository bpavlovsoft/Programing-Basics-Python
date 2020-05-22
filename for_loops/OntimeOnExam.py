exam_hours = int(input())
exam_minute = int(input())
arraival_hour = int(input())
arraival_minute = int(input())
late = "Late"
on_time = "On Time"
early = "Early"
exam_time = (exam_hours * 60) + exam_minute
arraival_time = (arraival_hour * 60) + arraival_minute
total_minutes = arraival_time - exam_time
student_arraival = late
if total_minutes < -30:
    student_arraival = early
elif total_minutes <= 0:
    student_arraival = on_time
result = ""
if total_minutes != 0:
    hours_diff = abs(total_minutes) // 60
    minutes_diff = abs(total_minutes) % 60
    if hours_diff > 0:
        result = f"{hours_diff}:{minutes_diff:02} hours"
    else:
        result = f"{minutes_diff} minutes"
    if total_minutes < 0:
        result += " before the start"
    else:
        result += " after the start"
print(student_arraival)
if result:
    print(result)                         