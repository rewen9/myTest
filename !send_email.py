import smtplib




from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendEmail(email, name):
    HOST = "smtp.gmail.com"
    SUBJECT = "Test email from Python"
    TO = "nikolas91@mail.ru"
    text = "Python 3.4 rules them all!"
    port_admin = 587
    host_admin = ""
    from_admin = ""
    pswd_admin = ""

    FROM = "sanntriss@gmail.com"

    BODY = "\r\n".join((
        "From: %s" % from_admin,
        "To: %s" % TO,
        "Subject: %s" % SUBJECT,
        "",
        text
    ))

    msg = MIMEMultipart()
    msg['From'] = from_admin
    msg['To'] = TO
    msg['Subject'] = "Заявка на перезвонить pestcontrol localtest"

    body = "Это пробное сообщение"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP(host_admin, port=port_admin)
    server.starttls()
    server.login(from_admin, pswd_admin)
    # server.connect(HOST, 465)
    server.ehlo()
    # server.ehlo()
    text = msg.as_string()
    server.sendmail(from_admin, TO, text)
    server.quit()
    open('tmpEmail.txt', 'tw').close()


sendEmail('emial', 'name')