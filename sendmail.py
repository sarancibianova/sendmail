# SAR 2022.01.26 envia un mail . Pruebas de Configuracion de este tema
import smtplib, ssl
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

smtp_server = "tribilin.telnet.com.ar"
port = 25  # For starttls
sender_email = "facturacion@laboratoriosnova.com"
receiver_email = "sarancibia@laboratoriosnova.com"  # Enter receiver address
cc_email = ['sarancibia@laboartoriosnova.com','arancibiasergio@gmail.com']
password = sys.argv[1]
now = datetime.now()
message = now.strftime("%H:%M:%S") + """\
Subject: Vamo lo pibe

This message is sent from Python."""
msg = MIMEMultipart()
#msg['From'] = sender_email
#msg['To'] = receiver_email
#msg['CC'] = cc_email
msg['Subject'] = "Prueba de Python .."
msg.attach(MIMEText(message, 'plain'))

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    #server.auth(False)
    server.ehlo() # Can be omitted
    #server.starttls(context=context) # Secure the connection
    server.starttls
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
    # TODO: Send email here
    #server.sendmail(sender_email, receiver_email, message)
    recipients = ['sarancibia@laboratoriosnova.com']
    cc_recipients = ['arancibiasergio@gmail.com', 'sistemas@laboratoriosnova.com']
    msg['To'] = ", ".join(recipients)
    msg['Cc'] = ", ".join(cc_recipients)
    msg['From'] = sender_email
    recipients.extend(cc_recipients)
    server.sendmail(msg['From'],recipients,msg.as_string())
    #server.sendmail(msg['From'], msg['To'], msg.as_string())
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit() 