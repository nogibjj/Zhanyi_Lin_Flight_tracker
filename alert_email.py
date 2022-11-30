import smtplib
from email.message import EmailMessage
def send_mail(dp,ds, to_email, subject, price, server='smtp.example.cn',
              from_email='563186832wayne@example.com'):
    # import smtplib
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = ', '.join(to_email)
    messgaae = "The flight price from {} to {} is lower than your expectation. Got to buy it! ".format(dp,ds)
    msg.set_content(message)
    print(msg)
    server = smtplib.SMTP(server)
    server.set_debuglevel(1)
    server.login('563186832wayne@example.com', 'Lzy200105JL7')  # user & password
    server.send_message(msg)
    server.quit()
    print('successfully sent the mail.')