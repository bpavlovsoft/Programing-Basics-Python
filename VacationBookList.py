count_pages = int(input())
pages_for_hour = int(input())
days = int(input())
total_hours = count_pages / pages_for_hour
result = total_hours / days
print(result)