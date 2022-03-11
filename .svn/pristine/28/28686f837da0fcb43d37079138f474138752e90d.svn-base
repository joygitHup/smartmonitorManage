import smtplib
from email.header import Header
from email.mime.text import MIMEText
from future.backports.email.mime.multipart import MIMEMultipart
class sendEmai():
    @staticmethod
    def Sendemail(newfile):
        f=open(newfile,'rb')
        mail_body=f.read()
        f.close()
        smtpserver = 'smtp.exmail.qq.com'
        user = 'irven@cloudeasetech.com'
        password = 'Laiyi1995823'
        sender="irven@cloudeasetech.com"
        # xuli@mogul-tech.com
        receiver=["irven@cloudeasetech.com"]
        subject='自动化测试报告'
        msg = MIMEMultipart('mixed')
        msg_html1 = MIMEText(mail_body,'html','utf-8')
        msg.attach(msg_html1)
        msg_html = MIMEText(mail_body,'html','utf-8')
        msg_html["Content-Disposition"] = 'attachment;filename="result.html"'
        msg.attach(msg_html)
        msg['From'] = 'irven@cloudeasetech.com'
        msg['To'] = ";".join(receiver)
        msg['Subject'] = Header(subject,'utf-8')
        smtp = smtplib.SMTP_SSL(smtpserver,465)
        # smtp.connect(smtpserver,465)
        smtp.login(user, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()