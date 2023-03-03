def subtract_time(hours, minutes):
    # Subtract 7 hours and 45 minutes
    hours   -= 7
    minutes -= 45

    # If minutes<0
    if (hours > 0 and minutes < 0):
        minutes += 60
        hours -= 1   

    elif (hours < 0 and minutes > 0): hours += 24

    elif (hours < 0 and minutes < 0):
        hours   += 23
        minutes += 60

    return hours, minutes

