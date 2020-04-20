# import packages
import smtplib
from GetData_API import*


def SendEmail(email):
    # add header
    message = "latest sports news update"

    # setup the parameters of the message
    password = 'uwobmiwtykeuqwla'
    msg['From'] = 'sportsnewstk@gmail.com'
    msg['To'] = email
    msg['Subject'] = "latest sports update"
    


    # message header and body
    header = MIMEText(message, 'plain')
    content = MIMEText(html, 'html')
   # image = MIMEText(html2, 'html')


    msg.attach(header)
    msg.attach(content)


    # create a server
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    # Login Credentials for sending the mail
    server.login(msg['From'], password)
    emails = ["sportsnewstk@gmail.com"]

    # send the message through the server.
    # for email in obj:
    server.sendmail(msg['From'], email, msg.as_string())
    print("successfully sent email to %s:" % email)
    server.quit()









