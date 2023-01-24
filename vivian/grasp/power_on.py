import smtplib, ssl

#email 

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "nicobwan@gmail.com"  # Enter your address
receiver_email = "offdutymanager@gmail.com"  # Enter receiver address
# password = input("Type your password and press enter: ")
password = "Loading@1"
message = """\
Subject: Raspberry Vivian

I have been powered on."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

