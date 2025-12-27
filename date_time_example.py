#"2024/12/15" string-ийг datatime руу хөрвүүлэх

import datetime as dt

# Get current datetime
now = dt.datetime.now()
print(now.strftime('%Y-%m-%d'))

# Create a specific date
my_date = dt.date(2024, 12, 5)
print(my_date.strftime('%y, %B %d'))

# Parse string to datetime (as per comment)
date_str = "2024/12/15"
parsed_date = dt.datetime.strptime(date_str, "%Y/%m/%d")
print(parsed_date.strftime('%Y-%m-%d'))


#Дээрх огноо нь дээр 7 өдрийг нэмбэл
new_data = parsed_date + dt.timedelta(days=7)
print(new_data.strftime('%Y-%m-%d'))

#Үр дүнг текст хэлбэртэй гаргавал

# Create a specific date
new_date = dt.date(2024, 12, 22)
print(new_date.strftime('%y, %B %d'))