# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2019-12-26 16:58
import smtplib
from email.mime.text import MIMEText

# 设置服务器所需信息
host = 'smtp.163.com'  # 163邮箱服务器地址
username = '15083158852@163.com'  # 163用户名
password = 'TGZJUHKFOLKWQBBT'  # 密码(部分邮箱为授权码)
sender = '15083158852@163.com'  # 邮件发送方邮箱地址
receivers = ['haiyu.ma@genomicarebio.com']  # 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发

# 设置email信息
# 邮件内容设置
message = MIMEText('测试报告内容', 'plain', 'utf-8')
# 邮件主题
message['Subject'] = '自动化测试报告'
# 发送方信息
message['From'] = sender
# 接受方信息
message['To'] = receivers[0]

# 登录并发送邮件
try:
    smtpObj = smtplib.SMTP()
    # 连接到服务器
    smtpObj.connect(host, 25)
    # 登录到服务器
    smtpObj.login(username, password)
    # 发送
    smtpObj.sendmail(sender, receivers, message.as_string())
    # 退出
    smtpObj.quit()
    print('Email send success!')
except smtplib.SMTPException as e:
    print('Email send error!', e)  # 打印错误

'''
注意事项：一些邮箱登录比如 QQ 邮箱需要 SSL 认证，所以 SMTP 已经不能满足要求，而需要SMTP_SSL，解决办法为：
#启动
smtpObj = smtplib.SMTP()
#连接到服务器
smtpObj.connect(mail_host,25)
#######替换为########
smtpObj = smtplib.SMTP_SSL(mail_host)
'''
