import smtplib

to = input("Enter the mail of the recipient:\n")

content = input("Enter the Content of the mail:\n")

def send_mail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("senderemail.com", '1234')
    server.sendmail("senderemail.com", to, content)
    server.close()


send_mail(to, content)
