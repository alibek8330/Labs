
import datetime
t = datetime.datetime.now()
yesterday = t - datetime.timedelta(days=1)
tomorrow = t + datetime.timedelta(days=1)
print("Yesterday: " + yesterday.strftime('%Y-%m-%d'))
print("Today: " + t.strftime('%Y-%m-%d'))
print("Tomorrow: " + tomorrow.strftime('%Y-%m-%d'))

import datetime
t = datetime.datetime.now()
yesterday = t - datetime.timedelta(days=1)
tomorrow = t + datetime.timedelta(days=1)
print("Yesterday: " + yesterday.strftime('%Y-%m-%d'))
print("Today: " + t.strftime('%Y-%m-%d'))
print("Tomorrow: " + tomorrow.strftime('%Y-%m-%d'))

