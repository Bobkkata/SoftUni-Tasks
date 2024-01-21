hour_exam = int(input())
min_exam = int(input())
hour_arrival = int(input())
min_arrival = int(input())

exam_time_minutes = (hour_exam * 60) + min_exam #570
arrival_time_min = (hour_arrival * 60) + min_arrival #590

diff_min = abs(exam_time_minutes - arrival_time_min)

if arrival_time_min > exam_time_minutes:
    print("Late")
    if diff_min >= 60:
        hour = diff_min // 60
        minutes = diff_min % 60
        print(f'{hour}:{minutes:02d} hours after the start')
    else:
        print(f'{diff_min} minutest after the start')

elif arrival_time_min == exam_time_minutes or diff_min <= 30:
    print("On time")
    if diff_min > 0:
        print(f'{diff_min} minutes before the start')

elif arrival_time_min < exam_time_minutes:
    print("Early")
    if diff_min >= 60:
        hour = diff_min // 60
        minutes = diff_min % 60
        print(f'{hour}:{minutes} hours before the start')
    else:
        print(f'{diff_min} minutes before the start')


        #Преписана!!!!