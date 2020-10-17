from datetime import datetime

birthday = datetime(1996, 3, 21, 11, 23, 52)

now = datetime.now()

difference = datetime.now() - datetime(2020, 1, 1)

parsed_date = datetime.strptime('Jan 15, 2020', '%b %d, %Y')

date_string = datetime.strftime(datetime.now(), '%b %d, %Y')

print(date_string)
