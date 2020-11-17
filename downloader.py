from datetime import date, timedelta, datetime

import time

from downloader_get_report import get_report

# MDM5YzQxODUtMGZhNC00MzlkLThjYzktOGRlODAwMDVkY2Nh
# 039c4185-0fa4-439d-8cc9-8de80005dcca

'''ВИП Маркет
930c9ac6-4a88-4a51-8e43-7a444a102f8d 
Ключ Base64: OTMwYzlhYzYtNGE4OC00YTUxLThlNDMtN2E0NDRhMTAyZjhk
'''
key = 'OTMwYzlhYzYtNGE4OC00YTUxLThlNDMtN2E0NDRhMTAyZjhk'


sales = 'https://suppliers-stats.wildberries.ru/api/v1/supplier/sales'

# def get_from_date_for_sales_report():
#     if date.today().weekday() != 0:
#         dt = date.today() - timedelta(1)
#     else:
#         dt = date.today() - timedelta(7)
#     return dt
#
#
# def get_to_date_for_sales_report():
#     if date.today().weekday() != 0:
#         dt = date.today()
#     else:
#         dt = date.today() - timedelta(1)
#     return dt





def launch_reports(counter=None):
    dt = date(2020, 8, 17) + timedelta(counter)
    sales_params = {'key': {key},
                    'flag': 1,
                    'dateFrom': {dt}, 'dateTo': {dt},
                    # during date by default
                    'limit': 100_000, }
    date_str = dt.strftime("%Y-%m-%d")
    get_report(sales, sales_params, date_str)



def call_reports():
    counter = 0
    while counter < 91:
        try:
            print(f'call to API for report')
            launch_reports(counter)
        except:
            print('smth went wrong')
        counter += 1
        time.sleep(240)

call_reports()
# schedule.every(5).minutes(5).do(launch_reports)
# schedule.every(30).minutes.do(launch_reports)



