
# https://docs.python.org/3/library/datetime.html
import datetime
# from datetime import datetime
import time

# time
print(time.time())

print(time.localtime(time.time()))

print(datetime.datetime.now())
print(datetime.timedelta.max)



"""
object
    timedelta
    tzinfo
        timezone
    time
    date
        datetime
"""