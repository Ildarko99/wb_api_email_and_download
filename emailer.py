# Python code to illustrate Sending mail with attachments 
# from your Gmail account 

# libraries to be imported
import os
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

def emailer(from_email, from_email_pass, to_emails, sklad_report_filename=None, orders_report_filename=None,
            sales_report_filename=None, postavki_report_filename=None):
    print(f'trying email reports file')

    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = from_email

    # storing the receivers email address
    msg['To'] = to_emails

    # storing the subject
    msg['Subject'] = f"WB reports"

    # string to store the body of the mail
    body = ""

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))


    def load_file_to_msg(file, filename):
        # instance of MIMEBase and named as p
        payload = MIMEBase('application', 'octet-stream')

        # To change the payload into encoded form
        payload.set_payload(file.read())
        # encode into base64
        encoders.encode_base64(payload)
        payload.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        # attach the instance 'p' to instance 'msg'
        msg.attach(payload)
        print(f'{filename} attached')

    # open files to be sent
    # file
    sklad_report_xls = open(os.path.join(f'{sklad_report_filename}'), 'rb')
    sales_report_xls = open(os.path.join(f'{sales_report_filename}'), 'rb')
    orders_report_xls = open(os.path.join(f'{orders_report_filename}'), 'rb')
    postavki_report_xls = open(os.path.join(f'{postavki_report_filename}'), 'rb')

    # attach files
    load_file_to_msg(sklad_report_xls, sklad_report_filename)
    load_file_to_msg(sales_report_xls, sales_report_filename)
    load_file_to_msg(orders_report_xls, orders_report_filename)
    load_file_to_msg(postavki_report_xls, postavki_report_filename)

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(from_email, from_email_pass)
    print('email login ok')
    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(from_email, to_emails, text)
    print(f'Reports sent succesfull')
    # terminating the session
    s.quit()
