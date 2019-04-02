import imaplib
import datetime
import time
import os
import getpass

# Insert e-mail login data

uname = <insert your username>
passw = getpass.getpass('Enter your password:')

imapserv = <insert your imap>

mail = imaplib.IMAP4(imapserv)
mail.login(uname, passw)
mail.select()

# What should the message code for shutting down and which e-mail should it come from?

msg = <What kind of code should the msg subject have?>
mailaddr = <From what address should the message come?>

# How often should the inbox be checked (in secs)?

freqs = 60.0

# Messages dating until how many days ago should be taken into account?

dayssince = 1

# Start the loop

start = time.time()

while True:

    date = (datetime.date.today() - datetime.timedelta(dayssince)).strftime("%d-%b-%Y")

    result, data = mail.uid('search', None, '(SENTSINCE {date} HEADER Subject "'.format(date=date) + msg + '" FROM "' + mailaddr + '")')

    if data != [b'']:
        os.system('shutdown -s')
    else:
        print("No shutdown needed.")

    time.sleep(freqs - ((time.time() - start) % freqs))
