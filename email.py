import smtplib

sender = "saifanas718@gmail.com"
receiver = "saifanasyt06@gmail.com"
password = "qwerty123456789@0"
subject = "Python email test"
body = "I wrote an email! :D"

# HEADER
message = f"""From: Voldemort{sender}
To: {receiver}
Subject: {subject}\n
{body}
""" 

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender,password)
    print("Logged in...")
    server.sendmail(sender, receiver, message)
    print("Email has been sent!")

except smtplib.SMTPAuthenticationError:
    print("unable to sign in")