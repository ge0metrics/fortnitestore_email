import smtplib, ssl,os
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from datetime import date

def send_email():
    sender_email = "YOUR_SENDER_EMAIL"
    receiver_email = "YOUR_RECEIVING_EMAIL"
    password = "YOUR_SENDER_PASSWORD"

    date_=date.today().strftime("%B %d %Y")

    message=MIMEMultipart("alternative")
    message["Subject"]="Fortnite Store {}".format(date_)
    message["From"]=sender_email
    message["To"]=receiver_email

    attachments=os.listdir("./out/")
    for a in attachments:
        attachment="./out/{}".format(a)
        with open(attachment, 'rb') as fp:
            img = MIMEImage(fp.read())
        img.add_header('Content-ID', '<{}>'.format(attachment))
        message.attach(img)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )