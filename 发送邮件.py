import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import formataddr

msg=MIMEMultipart('related')
email_from_name=''
from_addr='haixxm'
password='NEFBxxxBot7'
to_addr=['9xx'] #收件邮箱(多个之间用逗号隔开)
cc_addr=['xxcom']  #抄送邮箱(多个之间用逗号隔开)
smtp_server = 'smtp.exmail.qq.com'
if cc_addr:
    receiver_addr=to_addr+cc_addr
else:
    receiver_addr=to_addr

msg['Subject']=Header("官网更新",'utf-8')
msg['From']=formataddr(pair=(email_from_name,from_addr))
msg['to']=';'.join(to_addr)
msg['Cc']=';'.join(cc_addr)

message='''
官网更新
'''

thebody=MIMEText(message,'plain','utf-8')
msg.attach(thebody)

try:
    server=smtplib.SMTP_SSL(smtp_server,465)
    server.login(from_addr,password)
    server.sendmail(from_addr,receiver_addr,msg.as_string())
    server.quit()
    print('邮件发送成功')
except smtplib.SMTPException as e:
    print('发送失败 case %s'%e)

