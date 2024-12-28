import smtplib
from smtplib import SMTP
from email.message import EmailMessage

def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('prasannachowdarymullapudi@gmail.com','lgci yewe nkvs rzri')
    msg=EmailMessage()
    msg['From']='prasannachowdarymullapudi@gmail.com'
    msg['Subject']=subject
    msg['To']='prasannachowdarymullapudi@gmail.com'
    msg.set_content(body)
    server.send_message(msg)
    server.quit()