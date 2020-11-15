import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def error_emailer(from_email, from_email_pass, to_emails):
    print(f'sending error message')

    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = from_email

    # storing the receivers email address
    msg['To'] = to_emails

    # storing the subject
    msg['Subject'] = f"WB reports got error"

    # string to store the body of the mail
    body = ""

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

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
    print(f'Error report sent succesfull')
    # terminating the session
    s.quit()
