# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2019-12-26 16:58
import smtplib
from email.mime.text import MIMEText  # 构建邮件文本

# 设置服务器所需信息
host = 'smtp.163.com'  # 163邮箱服务器地址
password = 'TGZJUHKFOLKWQBBT'  # 密码(部分邮箱为授权码)
sender = '15083158852@163.com'  # 邮件发送方邮箱地址
receivers = ['haiyu.ma@genomicarebio.com']  # 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
class SendEmail:
    """封装发送邮件的方法"""
    @staticmethod
    def send_mail(content):
        message = MIMEText(content, 'plain', 'utf-8')  # 设置email信息
        message['Subject'] = '自动化测试报告'  # 邮件主题
        message['From'] = sender  # 发送方信息
        message['To'] = receivers[0]  # 接受方信息
        # 登录并发送邮件
        try:
            smtpObj = smtplib.SMTP()
            # 连接到服务器
            smtpObj.connect(host, 25)
            # 登录到服务器
            smtpObj.login(sender, password)
            # 发送邮件，关闭连接
            smtpObj.sendmail(sender, receivers, message.as_string())  # :as_string()是将msg(MIMEText对象或者MIMEMultipart对象)变为str
            smtpObj.quit()
            print('Email send success!')
        except Exception as e:
            print('Email send error!')
            raise e