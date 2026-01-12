import datetime

now = datetime.datetime.now()

print("{:<15} {:<15} {:<15}".format("Date", "Time", "Year"))
print("{:<15} {:<15} {:<15}".format(
    now.strftime("%d-%m-%Y"),
    now.strftime("%H:%M:%S"),
    now.strftime("%Y")
))

print("{:<15} {:<15} {:<15}".format("Hour", "Minutes", "Seconds"))
print("{:<15} {:<15} {:<15}".format(
    now.strftime("%H"),
    now.strftime("%M"),
    now.strftime("%S")
))
