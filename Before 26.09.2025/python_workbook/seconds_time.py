seconds = int(input("Enter time in seconds: "))

seconds_per_day = 86400
seconds_per_hour = 3600
seconds_per_minute = 60

days = seconds // seconds_per_day
seconds %= seconds_per_day

hours = seconds // seconds_per_hour
seconds %= seconds_per_hour

minutes = seconds // seconds_per_minute
seconds %= seconds_per_minute

print("%d:%02d:%02d:%02d" %(days,hours,minutes,seconds))
