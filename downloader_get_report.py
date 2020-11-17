import json
import pathlib

import pandas
import requests
import pandas as pd
import os
import time


def get_report(url, params, report_date: str):
    # print(f'starting {report_date} report with {params} by {url}')
    report = requests.get(url, params=params,)

    print(os.path.join(f'report_{report_date} report status code:'), report.status_code)
    # print(report.json())

    with open(os.path.join(f'reports/{report_date}.json'), 'wb') as outf:
        outf.write(report.content)
        print(f'report_{report_date}.json is downloaded and saved')
    #converting json to xls with pandas
    with open(os.path.join(f'reports/{report_date}.json')) as json_file:
        pandas.read_json(json_file).to_excel(os.path.join('reports/', f'{report_date}.xlsx'))
        print(f'report_{report_date}.xlsx saved')
    file_to_remove = pathlib.Path(f'reports/{report_date}.json')
    file_to_remove.unlink()







