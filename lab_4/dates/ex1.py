
import datetime

date = datetime.datetime.now()
print(date.strftime("%Y-%m-%d"))

back_to_5days = date - datetime.timedelta(days=5)
import datetime

date = datetime.datetime.now()
print(date.strftime("%Y-%m-%d"))

back_to_5days = date - datetime.timedelta(days=5)
print("Date that was 5 days ago: " + str(back_to_5days.strftime("%Y-%m-%d")))