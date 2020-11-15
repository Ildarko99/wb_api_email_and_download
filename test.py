#!/usr/bin/python
import time
import schedule

def test():
    while True:
        print('im running')
        time.sleep(4)

# schedule.every(1).minutes.do(test)
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)