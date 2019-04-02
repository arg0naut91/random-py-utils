import smtplib
import getpass

smtpserv = <insertsmtpserver>
smtpport = <insertport>

uname = <insertloginuname>
passw = getpass.getpass('Enter your password:')

server = smtplib.SMTP(smtpserv, smtpport)
server.ehlo()
server.starttls()
server.login(uname, passw)

sendingmail = <insert sending mail>
receivingmail = <insert receiving mail>

# Write the message

msg = """From: <insert sender>
To: <insert receiver>
Subject: <insert subject>

<insert your msg>

"""
 
server.sendmail(sendingmail, receivingmail, msg)
