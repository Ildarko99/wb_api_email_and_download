from datetime import date, timedelta, datetime

import time

import schedule

from downloader_get_report import get_report

"""
Орион
MDM5YzQxODUtMGZhNC00MzlkLThjYzktOGRlODAwMDVkY2Nh
039c4185-0fa4-439d-8cc9-8de80005dcca

ВИП Маркет
930c9ac6-4a88-4a51-8e43-7a444a102f8d 
Ключ Base64: OTMwYzlhYzYtNGE4OC00YTUxLThlNDMtN2E0NDRhMTAyZjhk
"""
key = 'MDM5YzQxODUtMGZhNC00MzlkLThjYzktOGRlODAwMDVkY2Nh'

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
    start_date = date(2020, 11, 19) + timedelta(counter)
    sales_params = {'key': {key},
                    'flag': 1,
                    'dateFrom': {start_date}, 'dateTo': {start_date},
                    # during date by default
                    'limit': 100_000, }
    date_str = start_date.strftime("%Y-%m-%d")
    get_report(sales, sales_params, f'orion_{start_date}')


def call_reports():
    counter = 0
    while counter < 2:
        try:
            print(f'call to API for report')
            launch_reports(counter)
        except:
            print('smth went wrong')
        counter += 1
        print(f'counter={counter}')
        time.sleep(61)
        for i in range(1, 61):
            print(f'{i}, ', end='')
            time.sleep(1)


call_reports()

# schedule.every(1).minutes.do(call_reports)
# schedule.every(2).minutes.do(call_reports)
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)