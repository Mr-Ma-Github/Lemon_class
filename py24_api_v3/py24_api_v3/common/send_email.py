"""
============================
Author:柠檬班-木森
Time:2019/12/16
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication




def send_msg(file_path):

    # 第一步： 连接到smtp服务器
    smtp = smtplib.SMTP_SSL("smtp.qq.com",465)
    smtp.login("musen_nmb@qq.com","algmmzptupjccbab")

    # 第二步：构建邮件
    smg = MIMEMultipart()

    text_smg = MIMEText(open(file_path,'r',encoding='utf8').read(),"html")
    smg.attach(text_smg)

    file_msg = MIMEApplication(open(file_path,"rb").read())
    file_msg.add_header('content-disposition', 'attachment', filename='report.html')
    smg.attach(file_msg)

    smg["Subject"] = "24期报告"
    smg["From"] = "musen_nmb@qq.com"
    smg["To"] = "musen_nbm@163.com"

    # 第三步发送邮件
    smtp.send_message(smg,from_addr="musen_nmb@qq.com",to_addrs="musen_nbm@163.com")

