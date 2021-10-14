import datetime
import time
time1=input("Enter time in format of Hour:Minutes:Seconds please : ")
x = time.strptime(time1,'%H:%M:%S')
time_in_seconds = datetime.timedelta(hours = x.tm_hour,minutes = x.tm_min,seconds = x.tm_sec).total_seconds()
print("Time in second is : ",time_in_seconds)