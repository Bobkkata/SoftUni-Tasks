number_pages = int(input())
pages = int(input())
number_days = int(input())

time_to_read = number_pages // pages
time_of_day = time_to_read // number_days

print(time_of_day)

