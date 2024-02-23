from datetime import datetime

# date_string = input("YYYY-MM-DD: ")
# date_object = datetime.strptime(date_string, '%Y-%m-%d')
# print(date_object.strftime('%Y-%m-%d'))

print('Input date as YYYY-MM-DD')
first = input('First: ')
second = input('Second: ')
first_date = datetime.strptime(first, '%Y-%m-%d')
second_date = datetime.strptime(second, '%Y-%m-%d')
diff_dates = second_date - first_date
seconds_diff = diff_dates.total_seconds()
print("The difference between the two dates is: " + str(abs(int(seconds_diff))) + " seconds")