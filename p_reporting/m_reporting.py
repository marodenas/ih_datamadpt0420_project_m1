import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import configparser
import pysftp
from p_wrangling import m_wrangling as mwr


# reporting functions


def save_viz(fig, title):
    fig.savefig('./data/results/' + title + '.png')


def save_csv(df, country):
    if not country:
        country = "All"
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d-%H-%M")
    df.to_csv(f'data/results/{country}-{dt_string}.csv', index=False)
    location = f'data/results/{country}-{dt_string}.csv'
    return location


def send_email(location):
    cfg = configparser.RawConfigParser()
    cfg.read('config.ini')
    mail_content = ''' <html><table style="background:#efefef" width="100%" cellspacing="0" cellpadding="0" border="0" align="center"><tbody> <tr> <td> <table width="600" cellspacing="0" cellpadding="0" border="0" align="center"> <tbody> <tr> <td>&nbsp;</td> </tr> <tr> <td style="font-family:Verdana,Geneva,sans-serif;padding-bottom:10px;font-size:12px;color:#777777" align="center">Data Analysis by Miguel Ángel Ródenas</td> </tr> <tr> <td>&nbsp;</td> </tr> <tr> <td> <table style="background-color:#ffffff;text-align:center" width="100%" cellspacing="30" cellpadding="0" border="0" align="center"> <tbody> <tr> <td style="font-family:Verdana,Arial,sans-serif;padding:20px 30px;font-size:14px;line-height:20px;color:#000;text-align:center"> <h1>Here is your report requested!</h1> <p>In this email you will find the report.<br>Feel free to contact me if you have any question. </p> <p style="color:#4df7b9;font-weight: bold;">See the file attached</p> </td> </tr> </tbody> </table> </td> </tr> <tr> <td height=50>&nbsp;</td> </tr> </tbody> </table> </td> <tr> </tr> </tr> </tbody></table></html>
    '''
    # The mail addresses and password
    sender_address = cfg['email']['user']
    sender_pass = cfg['email']['password']
    receiver_address = cfg['email']['receiver']
    receiver_address_l = receiver_address.split(',')
    # print(type(receiver_address))
    for email in receiver_address_l:
        # Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = email
        message['Subject'] = 'Here are your reports!'
        # The subject line
        # The body and the attachments for the mail
        message.attach(MIMEText(mail_content, 'html'))
        attach_file_name = 'report'
        for file in location:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(open(file, 'rb').read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="%s"' % file[13:])
            message.attach(part)

        session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
        # session.starttls()  # enable security

        session.ehlo()
        session.starttls()
        session.login(sender_address, sender_pass)  # login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, email, text)
        session.quit()
    print('Mail Sent')

def upload_to_website(location):
    new_loc = mwr.csv_to_html(location)
    cfg = configparser.RawConfigParser()
    cfg.read('config.ini')
    myHostname = cfg['website']['myHostname']
    myUsername = cfg['website']['myUsername']
    myPassword = cfg['website']['myPassword']
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    with pysftp.Connection(myHostname, username=myUsername, password=myPassword,cnopts=cnopts) as sftp:
        print("Connection succesfully stablished ... ")

        # Define the file that you want to upload from your local directorty
        localFilePath = new_loc

        # Define the remote path where the file will be uploaded
        remoteFilePath = '/web/'
        for x in localFilePath:
            sftp.put(x, remoteFilePath+x)

