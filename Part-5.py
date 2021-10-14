time_in_seconds = abs(int(input("Please enter time in Second : ")))
second = time_in_seconds % (24 * 3600)
hour = second // 3600
second %= 3600
minute = second // 60
second %= 60
print(time_in_seconds, " seconds has been converted to : ", "%02d:%02d:%02d" % (hour, minute, second),"(hour:minute:second)")