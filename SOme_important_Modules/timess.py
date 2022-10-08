from datetime import datetime
from email.utils import localtime
import imp
from operator import imod
from sqlite3 import Date
from time import strftime, time


from time import localtime,time

print(time())

print(localtime())

print(localtime())

# print(localtime().ctime())

# print(localtime().time())

obj=localtime()

print(obj.tm_year)


# datetime module

obj=datetime(2022,1,27)

print(obj)

print(datetime.now())    # time now


from datetime import date
# date class

print(date(2022,3,21))


from datetime import time
# time class

print(time(3,4,45))



# timedelta
from datetime import timedelta   # when we need to add substract data/time

td=timedelta(days=10)
d=date.today()
print(d+td)


# Compairing dates

print(date(2022,2,3)==date(2022,2,3))



# Formatting Date / Time

print(strftime(date(2022,3,22)))