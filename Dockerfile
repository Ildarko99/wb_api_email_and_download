FROM python:3.9.0b4-alpine3.12

COPY root /var/spool/cron/crontabs/root

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY . /usr/src/app/

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x /usr/src/app/test.py
CMD crond -l 2 -f




#ENV TZ Europe/Moscow