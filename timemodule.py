import time

# print(time.ctime(0))            # convert a time expressed in seconds since epoch to a redeable string
#                                 epoch = when your computer thinks time began (refrence point)

# print(time.time())              # return current seconds since epoch

# print(time.ctime(time.time()))

# time_object = time.localtime()
# time_object = time.gmtime()
# # print(time_object)

# local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)

# print(local_time)

# time_string = "20 April, 2023"
# time_object = time.strptime(time_string, "%d %B, %Y")
# print(time_object)

# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
time_tuple = (2023, 1, 3, 4, 20, 0, 0, 0, 0)
time_string = time.asctime(time_tuple)
print(time_string)  


# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
time_tuple = (2023, 1, 3, 4, 20, 0, 0, 0, 0)
time_string = time.mktime(time_tuple)
print(time_string)  