def add_time(initial, duration, day=False):

    initial_time = initial.split(":")  # Split at : so there are only digits
    initial_mins = initial_time[1].split(" ")  # Split at " " and grab the digit at index 1

    ## inhr, inms = initial.split(":")
    inhr = initial_time[0]  # Grab initial hrs from initial_time at index 0
    inms = initial_mins[0]  # Grab initial mins from initial_mins at index 0
    inampm = initial_mins[1]  # Grab initial AM/PM from initial_mins at index 1
    inhrint = int(inhr)  # Making the intial hr as an interger
    inmsint = int(inms)  # Making the intial mins as an interger

    duration_time = duration.split(":")  # Split duration at : so there are only digits

    dur_hrs = duration_time[0]  # Grab duration hours from duration_time index 0
    dur_mins = duration_time[1]  # Grab duration mins from duration_time index 0
    dur_hrsint = int(dur_hrs)  # Making the duration hr as an interger
    dur_minsint = int(dur_mins)  # Making the duration min as an interger

    days = 0
    one_day = 24
    half_day = 12

    # Calculate total hours and minutes
    calc_mins = inmsint + dur_minsint
    calc_hrs = inhrint + dur_hrsint

    # shift minutes  to hour if its over 60
    if calc_mins >= 60:
        calc_hrs += calc_mins / 60
        calc_mins = calc_mins % 60

    if "PM" in initial:
        if (inhrint + dur_hrsint) > 12:
            inampm = "AM"

    if "AM" in initial:
        if (inhrint + dur_hrsint) > 12:
            inampm = "PM"

    if "PM" in initial and inhrint + dur_hrsint >= 12:
        if calc_hrs % 24 >= 1:
            days += 1

    calc_hrs_str = str(calc_hrs)
    calc_mins_str = str(calc_mins)
    days_str = str(days)

    calc_text = calc_hrs_str + ":" + calc_mins_str + " " + inampm + " (" + days_str + " days later)"

    return calc_text


print(add_time("12:43 PM", "14:25"))
