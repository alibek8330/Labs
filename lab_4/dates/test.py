from datetime import datetime, timedelta

date_str = input()
date_time = datetime.strptime(date_str, "%d-%m-%Y")
back_to_5days = date_time - timedelta(days = 5)
formatted_result = back_to_5days.strftime("%d-%m-%Y")
print(formatted_result)