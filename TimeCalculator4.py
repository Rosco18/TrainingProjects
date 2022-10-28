def add_time(initial, duration, day=None):

    # Getting useful data from start string
    timely, midday = initial.split()
    hour, minutes = timely.split(':')
    hour = int(hour)
    minutes = int(minutes)

    # Making the clock into 24 hour format
    if midday == "PM":
        hour += 12

    # Getting data from duration
    duration_hour, duration_minutes = duration.split(':')
    duration_hour = int(duration_hour)
    duration_minutes = int(duration_minutes)

    # Calculating total hours, minutes
    total_minutes = minutes + duration_minutes
    ans_minutes = total_minutes % 60
    extra_hours = total_minutes // 60
    total_hour = hour + duration_hour + extra_hours

    # final hours as per 12 Hour clock
    ans_hour = (total_hour % 24) % 12

    # Edge case
    if ans_hour == 0:
        ans_hour = 12
    ans_hour = str(ans_hour)

    # total days 24 hr 1 day
    total_day = (total_hour // 24)

    # deciding mid day (AM/PM)
    ans_midday = ""
    if (total_hour % 24) <= 11:
        ans_midday = "AM"
    else:
        ans_midday = "PM"

    # Handling single digit minutes case
    if ans_minutes <= 9:
        ans_minutes = '0' + str(ans_minutes)
    else:
        ans_minutes = str(ans_minutes)

    # returning logic
    time_stamp = ans_hour + ":" + ans_minutes + ' ' + ans_midday

    return time_stamp, ans_hour, total_hour, total_day


print(add_time("11:43 PM", "10:10"))
