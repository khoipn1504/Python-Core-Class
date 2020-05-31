import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

try:
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login('hoiquanbienhoa.channel@gmail.com', 'Wywcorp868879')

    msg = MIMEMultipart()       # create a message
    msg['From'] = 'hoiquanbienhoa.channel@gmail.com'
    msg['To'] = 'tbtoanit@gmail.com'
    msg['Subject'] = "This is Notepad.txt file"

    s.send_message(msg)
    s.quit()
    print('Đã gui được')
except:
    print('Chưa gui được email')
