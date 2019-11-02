import smtplib
import sys                     

txtparam = sys.argv[0]

fromaddr = 'Svetlana <demonbydeath@mail.ru>'
toaddr = 'Svetlana <ksv98@inbox.ru>'
subj = 'Notification from system'

msg_txt = 'Notice:\n\n ' +  txtparam + '\n\nBye!' #
#Создаем письмо (заголовки и текст)
msg = "From: %s\nTo: %s\nSubject: %s\n\n%s"  % ( fromaddr, toaddr, subj, msg_txt)


username = 'demonbydeath'
password = 'bloodandsoul'

server = smtplib.SMTP_SSL('smtp.mail.ru:465')
server.set_debuglevel(1)
server.login(username, password)
server.sendmail(fromaddr, toaddr, msg)
server.quit()