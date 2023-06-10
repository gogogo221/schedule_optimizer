def time_to_min(time):
    hour = int(time[0:2])
    minute = int(time[3:5]) 
    minute += hour*60
    return minute
