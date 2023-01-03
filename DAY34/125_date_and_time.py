print("\n\n\n\n\n")
import time
print(time.time())

print(time.ctime())

time.sleep(10)
print(time.ctime())

print(time.localtime(1658672956.8853111))

print(time.gmtime(1658672956.8853111))

local_time = (2022, 7, 24, 20, 14, 39, 6, 205, 0)
print(time.mktime(local_time))


local_time = (2022, 7, 24, 20, 14, 39, 6, 205, 0)
print(time.asctime(local_time))


import calendar

print(calendar.month(2022, 7))

print("\n\n\n\n\n")




time.sleep(20)