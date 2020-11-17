from datetime import datetime, timedelta, date
import time
# x = 0
# dt = datetime(2020, 8, 17)
# while x <= 91:
#     dt += timedelta(1)
#     print(dt)
#     x += 1

dt = date(2020, 8, 17) - timedelta(118)
print(type(dt))
date_str = dt.strftime("%Y-%m-%d")
print(date_str)