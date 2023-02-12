from commandtaker import cmndtkr as brixy
import os
import wikipedia
import webbrowser
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

#This function can send email to any email address (working function)
def SendEmail(to, compose):
    # d = "454433453338363741434330453037433335313145414330323346393030463235374231"
    # e = "627269787079617373697374616E7440676D61696C2E636F6D"
    # cow = base64.b16decode(e).decode("utf-8")
    # Sheep = base64.b16decode(d).decode("utf-8")
    msg = MIMEMultipart()
    msg['Subject'] = 'New Message From Brixpy Assistant'
    msg['From'] = "brixpyassistant@gmail.com"
    # msg['To'] = to = "mahfuzrahman038@gmail.com"
    # compose = MIMEText("")
    msg.attach(compose);
    UserName = "brixpyassistant@gmail.com"
    UserPassword = "F411EDE86A2AFC0EF8C011346E8DC2366E34"
    Server = "smtp.elasticemail.com"
    Port = "2525"
    s = smtplib.SMTP(Server, Port)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(UserName, UserPassword)
    s.sendmail(UserName, to, msg.as_string())
    s.quit()

