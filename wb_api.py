from datetime import date, timedelta
from clean_folder import clean_folder
from emailer import emailer
from get_report import get_report
import time
from error_email import error_emailer
import schedule
# MDM5YzQxODUtMGZhNC00MzlkLThjYzktOGRlODAwMDVkY2Nh
# 039c4185-0fa4-439d-8cc9-8de80005dcca

date_str = time.strftime("%Y-%m-%d")  # using in filenames and reports params
key = 'MDM5YzQxODUtMGZhNC00MzlkLThjYzktOGRlODAwMDVkY2Nh'
to_emails = "ildar.yakhin@gmail.com"  # you can add adresses separated by ;
from_email = "ildar.python@gmail.com"  # gmail only
from_email_pass = "wbpython12345!"

postavki = 'https://suppliers-stats.wildberries.ru/api/v1/supplier/incomes'
sales = 'https://suppliers-stats.wildberries.ru/api/v1/supplier/sales'
sklad = 'https://suppliers-stats.wildberries.ru/api/v1/supplier/stocks'
orders = 'https://suppliers-stats.wildberries.ru/api/v1/supplier/orders'
realize = 'https://suppliers-stats.wildberries.ru/api/v1/supplier/reportDetailByPeriod'



# for sklad report
"""
Методы сервиса. Склад.
При получении данных Вы указываете в запросе дату и время (dateFrom), от которых выгружается информация (по «дата/время обновления информации в сервисе»).
Сервис статистики не хранит историю остатков товаров, поэтому получить данные об остатках товаров на прошедшую, не сегодняшнюю, дату невозможно.
Можно получить данные только на момент запроса к API.

Пояснение количественных полей:
• Quantity — "количество, доступное для продажи" —
доступно на сайте, можно добавить в корзину.
•
quantityFull — "количество полное" — то, что не
продано (числится на складе)
•
quantityNotInOrders — "количество не в заказе" —
числится на складе, и при этом не числится в
незавершенном заказе.

• Данные обновляются 3 раза в день - в 6-15, 11-20 и в
16-20. (Точное время отображается в поле
lastChangeDate) 
"""
sklad_params = {'key': {key},
                'flag': 0, 'dateFrom': {date_str},  # during date by default
                'limit': 100_000, }

# for sales report
"""
Методы сервиса. Продажи.
Если параметр flag=0 (или не указан в строке запроса), при вызове API возвращаются данные у которых значение
поля lastChangeDate (дата время обновления информации в сервисе) больше переданного в вызов значения
параметра dateFrom. При этом количество возвращенных строк данных варьируется в интервале от 0 до примерно
100000.
Если параметр flag = 1, то будет выгружена информация обо всех заказах или продажах с датой равной переданному
параметру dateFrom (в данном случае время в дате значения не имеет). При этом количество возвращенных строк
данных равно количеству всех заказов или продаж, сделанных в дате, переданной в параметре dateFrom.
Также в продажах выгружаются возвраты (количество/цена со знаком минус).
• Формула вычисления pricewithdisc:
Pricewithdisc = totalprice*((100 – discountPercent)/100 ) *((100 – promoCodeDiscount)/100 ) *((100 – spp)/100 )
Важно: Гарантируется хранение данных продаж не более 90 дней от текущей даты.
• Архивные данные (продажи с датами ранее 90 дней от текущей даты) нужно загружать по датам, с
параметром flag = 1.
• Данные обновляются 1 раз в 30 минут. (Точное время отображается в поле lastChangeDate)
• Каждое 3-е число месяца происходит пересчёт данных API за предыдущий месяц, в результате чего
происходит корректировка данных. В связи с этим рекомендуем перезагружать данные API каждый месяц
за предыдущий 4-го числа.
"""

if date.today().weekday() != 0:
    dt = date.today() - timedelta(1)
    dt2 = date.today()
else:
    dt = date.today() - timedelta(7)
    dt2 = date.today() - timedelta(1)

sales_params = {'key': {key},
                'flag': 1,
                'dateFrom': {dt}, 'dateTo': {dt2},  # during date by default
                'limit': 100_000, }  # 'rrdid': 10,

# orders params
"""
Методы сервиса. Заказы.
Если параметр flag=0 (или не указан в строке запроса), при вызове API возвращаются данные у которых значение поля lastChangeDate (дата время обновления информации в
сервисе) больше переданного в вызов значения параметра dateFrom. При этом количество возвращенных строк данных варьируется в интервале от 0 до примерно 100000.
Если параметр flag = 1, то будет выгружена информация обо всех заказах или продажах с датой равной переданному параметру dateFrom (в данном случае время в дате
значения не имеет). При этом количество возвращенных строк данных равно количеству всех заказов или продаж, сделанных в дате, переданной в параметре dateFrom.

totalPrice*(100-discountPercent)/100= pricewithdisc (как и Методах
сервиса. Продажи)
Важно: Гарантируется хранение данных заказов не более 90 дней от
текущей даты.
• Архивные данные (заказы с датами ранее 90 дней от текущей даты)
нужно загружать по датам, с параметром flag = 1.
• Данные обновляются 1 раз в 30 минут. (Точное время отображается в
поле lastChangeDate)
• Каждое 3-е число месяца происходит пересчёт данных API за
предыдущий месяц, в результате чего происходит корректировка
данных. В связи с этим рекомендуем перезагружать данные API
каждый месяц за предыдущий 4-го числа.
"""
orders_params = {'key': {key},
                 'dateFrom': {date_str}, }  # during date by default  # 'rrdid': 10, 'flag': 0,

# postavki params
"""
Методы сервиса. Заказы.
Если параметр flag=0 (или не указан в строке запроса), при вызове API возвращаются данные у которых значение поля lastChangeDate (дата время обновления информации в
сервисе) больше переданного в вызов значения параметра dateFrom. При этом количество возвращенных строк данных варьируется в интервале от 0 до примерно 100000.
Если параметр flag = 1, то будет выгружена информация обо всех заказах или продажах с датой равной переданному параметру dateFrom (в данном случае время в дате
значения не имеет). При этом количество возвращенных строк данных равно количеству всех заказов или продаж, сделанных в дате, переданной в параметре dateFrom.

totalPrice*(100-discountPercent)/100= pricewithdisc (как и Методах
сервиса. Продажи)
Важно: Гарантируется хранение данных заказов не более 90 дней от
текущей даты.
• Архивные данные (заказы с датами ранее 90 дней от текущей даты)
нужно загружать по датам, с параметром flag = 1.
• Данные обновляются 1 раз в 30 минут. (Точное время отображается в
поле lastChangeDate)
• Каждое 3-е число месяца происходит пересчёт данных API за
предыдущий месяц, в результате чего происходит корректировка
данных. В связи с этим рекомендуем перезагружать данные API
каждый месяц за предыдущий 4-го числа.
"""
dt = date.today() - timedelta(10)  # timedelta - how many days ago from today start looking for
postavki_params = {'key': {key},
                   'dateFrom': {dt}, }  # during date by default


def launch_reports():
    clean_folder()
    sklad_report = get_report(sklad, sklad_params, 'sklad')
    time.sleep(3)
    sales_report = get_report(sales, sales_params, 'orders')
    time.sleep(3)
    orders_report = get_report(orders, orders_params, 'sales')
    time.sleep(3)
    postavki_report = get_report(postavki, postavki_params, 'postavki')
    try:
        print(f'call to emailer')
        emailer(from_email, from_email_pass, to_emails, sklad_report, sales_report, orders_report, postavki_report)
    except:
        print('smth went wrong')
        error_emailer(from_email, from_email_pass, to_emails, )

    clean_folder()  # cleaning workfolder

schedule.every().day.at("17:58").do(launch_reports)

while True:
    schedule.run_pending()
    time.sleep(1)