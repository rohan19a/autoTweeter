import smtplib
from email.mime.text import MIMEText


def send_email_gmail(subject, message, destination):
    smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
    smtp_ssl_port = 465
    username = 'tweetupdaterbot@gmail.com'
    password = 'vpxxovygzvsuvprc'
    sender = 'tweetupdaterbot@gmail.com'
    targets = [x for x in destination]
    msg = MIMEText('Hi, how are you today?')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(targets)

    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    server.login(username, password)
    server.sendmail(sender, targets, msg.as_string())
    server.quit()

send_email_gmail('Test subject', 'This is the message', ['arohan19@gmail.com'])