import time

def test():
    while True:
        timestr = time.strftime("%d-%m-%s")
        print(timestr)
        time.sleep(1)