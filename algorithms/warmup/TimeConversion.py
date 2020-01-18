import time

def time_conversion(s):
    time_values = time.strptime(s, "%I:%M:%S%p")
    return time.strftime("%H:%M:%S", time_values)
