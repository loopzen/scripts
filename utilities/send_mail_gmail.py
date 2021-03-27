#!/usr/bin/python3
# -*- coding: UTF-8 -*-
##################################################
# SEND MAILS WITH GMAIL ACCOUNT
# Requires to active google option about less secure apps
# PARAMS:
#     1 - TO
#     2 - ASUNT
#     3 - MESSAGE
#     4 - <FULL PATH TO ATTACHMENT>
# Example: send_mail_gmail.py "email@gmail.com" "asunto" "$(cat ~/texto.md)"
##################################################
import os
import sys
import configparser
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_mail(to_address, subject, cuerpoMensaje):

    HOME_FOLDER = os.path.expanduser("~/")
    config = configparser.ConfigParser()
    config.read(HOME_FOLDER + "src/conf/loopzen.ini")
    if config.has_option("GMAIL", "ACCOUNT"):
        from_address = config["GMAIL"]["ACCOUNT"] + " "
    if config.has_option("GMAIL", "PASSWORD2"):
        password = config["GMAIL"]["PASSWORD2"] + " "
 
    # TEXTO
    message = MIMEMultipart()
    # CREDENTIALS
    message['From'] = from_address
    message['To'] = to_address
    message['Subject'] = subject
    message.attach(MIMEText(cuerpoMensaje, 'plain'))
    # SERVER
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(from_address, password)
    text=message.as_string()
    server.sendmail(from_address, to_address, text)
    server.quit()


def send_mail_with_attachement(to_address, subject, cuerpoMensaje, attachment):
    HOME_FOLDER = os.path.expanduser("~/")
    config = configparser.ConfigParser()
    config.read(HOME_FOLDER + "src/conf/loopzen.ini")
    if config.has_option("GMAIL", "ACCOUNT"):
        from_address = config["GMAIL"]["ACCOUNT"] + " "
        print(from_address)
    if config.has_option("GMAIL", "PASSWORD2"):
        password = config["GMAIL"]["PASSWORD2"] + " "
        print(password)

    # TEXTO
    message = MIMEMultipart()
    # CREDENTIALS
    message['From'] = from_address
    message['To'] = to_address
    message['Subject'] = subject
    message.attach(MIMEText(cuerpoMensaje, 'plain'))

    # ATTACHMENT
    part = MIMEBase('application', 'octet-stream')
    attachment=open(sys.argv[4], "rb")
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    message.attach(part)

    # SERVER
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(from_address, password)
    text=message.as_string()
    server.sendmail(from_address, to_address, text)
    server.quit()

def main():
    numero_parametros = len(sys.argv) - 1
    if numero_parametros == 3:
        to_address = sys.argv[1]
        subject = sys.argv[2]
        cuerpoMensaje = sys.argv[3]
        send_mail(to_address, subject, cuerpoMensaje)
    elif numero_parametros == 4:
        to_address = sys.argv[1]
        subject = sys.argv[2]
        cuerpoMensaje = sys.argv[3]
        filename = sys.argv[4]
        send_mail_with_attachement(to_address, subject, cuerpoMensaje, filename)
    else:
        print("To, Subject and Message are obligatios")

if __name__ == '__main__':
    main()
