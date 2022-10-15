import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailAccount:
    def __init__(self, login: str, password: str, subject: str, gmail_smtp: str, gmail_imap: str):
        self.login = login
        self.password = password
        self.subject = subject
        self.gmail_smtp = gmail_smtp
        self.gmail_imap = gmail_imap

    def send_message(self, recipients: list, massage: str or int):
        msg = MIMEMultipart()

        # message parameter definition
        msg['From'] = self.login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = self.subject

        # add in the message body
        msg.attach(MIMEText(massage))

        ms = smtplib.SMTP(host=self.gmail_smtp, port=587)

        # identify ourselves to smtp gmail client
        ms.ehlo()
        # secure our email with tls encryption
        ms.starttls()
        # re-identify ourselves as an encrypted connection
        ms.ehlo()

        ms.login(self.login, self.password)
        ms.sendmail(from_addr=self.login, to_addrs=msg['To'], msg=msg.as_string())

        ms.quit()

    def receive(self, headers=None) -> str:
        mail = imaplib.IMAP4_SSL(self.gmail_imap)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("INBOX")
        criterion = '(HEADER Subject "%s")' % headers if headers else 'ALL'
        result, data = mail.uid('search', criterion)

        # There are no letters with current header
        assert data[0]

        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()

        return email_message['Subject']

