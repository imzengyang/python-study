
# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

textfile='test.html'
# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
with open(textfile,encoding='utf8') as fp:
    # Create a text/plain message
    msg = MIMEText(fp.read(),'html','utf-8')

me = "15505919313@163.com"
you = "390021310@qq.com"
msg['Subject'] = 'The contents of %s' % textfile
msg['From'] = me
msg['To'] = you

username="15505919313@163.com"
passwd="xxx"
smtphost="smtp.163.com"

# Send the message via our own SMTP server.
s = smtplib.SMTP_SSL(smtphost)
s.login(username,passwd)
s.sendmail(me,you,msg.as_string())
s.quit()