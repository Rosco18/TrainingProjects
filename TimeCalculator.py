def add_time(initial, duration, day=False):

    initial_time = initial.split(":")
    initial_mins = initial_time[1].split(" ")

    ## inhr, inms = initial.split(":")
    inhr = initial_time[0]
    inms = initial_mins[0]
    inampm = initial_mins[1]
    inhrint = int(inhr)
    inmsint = int(inms)

    duration_time = duration.split(":")

    dur_hrs = duration_time[0]
    dur_mins = duration_time[1]
    dur_hrsint = int(dur_hrs)
    dur_minsint = int(dur_mins)

    return inampm


print(add_time("12:43 PM", "8:25"))
