days = int(input("How many days? "))
hours = int(input("How many hours? "))
minutes = int(input("How many minutes? "))
seconds = int(input("How many seconds? "))

print(days*24*60*60 + hours*60*60 + minutes*60 + seconds, "seconds")
