import json
import requests
import pandas as pd
import os
import time


def get_report(url, params, report_name: str):
    print(f'starting {report_name} report with {params} by {url}')
    report = requests.get(url, params=params,)

    print(os.path.join(f'files/{report_name} report status code:'), report.status_code)
    # print(report.json())

    with open(os.path.join(f'files/{report_name}.json'), 'wb') as outf:
        outf.write(report.content)
        print(f'files/{report_name}.json')

    with open(os.path.join(f'files/{report_name}.json')) as json_file:
        data = json.load(json_file)
        print(f'files/{report_name}.json loaded')

    date_str = time.strftime("%Y-%m-%d")

    #converting json to xls with pandas
    df = pd.DataFrame(data)
    df.to_excel(os.path.join(f'files/{report_name}_{date_str}.xlsx'))
    print(f'files/{report_name}_{date_str}.xlsx saved')
    filename = f'files/{report_name}_{date_str}.xlsx'
    # os.remove(f'files/{report_name}.json')
    # print(f'files/{report_name}.json removed')
    return filename


