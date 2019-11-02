import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
fromaddr = "demonbydeath@mail.ru"
toaddr = "ksv98@inbox.ru"
mypass = "5273925bB"
 
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Миракаст"
 
body = "Это пробное сообщение"
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
server.starttls()
server.login(fromaddr, mypass)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()