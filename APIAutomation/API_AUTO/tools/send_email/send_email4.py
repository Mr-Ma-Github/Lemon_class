# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2019-12-26 16:58
# coding: utf-8
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# 设置smtplib所需的参数
host = 'smtp.163.com'  # 163邮箱服务器地址
password = 'TGZJUHKFOLKWQBBT'  # 密码(部分邮箱为授权码)
sender = '15083158852@163.com'  # 邮件发送方邮箱地址
receivers = ['haiyu.ma@genomicarebio.com']  # 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发

class SendEmail:
    def send_email(self, report_path=None):
        # 构造邮件对象MIMEMultipart对象
        msg = MIMEMultipart('mixed')
        msg['Subject'] = '自动化测试报告'  # 邮件主题
        msg['From'] = sender  # 发送方信息
        msg['To'] = ','.join(receivers)

        # 构造文字内容
        text = "Hello!\nThis is a Interface automation test report:\nhttp://www.baidu.com"
        text_plain = MIMEText(text, 'plain', 'utf-8')
        msg.attach(text_plain)

        # 构造附件
        if report_path:
            text_att = MIMEText(open(report_path, 'rb').read(), 'base64', 'utf-8')
            text_att.add_header('Content-Disposition', 'attachment', filename='test_report.html')
            msg.attach(text_att)
        else:
            pass

        # 发送邮件
        try:
            smtp = smtplib.SMTP()
            smtp.connect(host, 25)
            # 我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
            # smtp.set_debuglevel(1)
            smtp.login(sender, password)
            smtp.sendmail(sender, receivers, msg.as_string())  # 必须和msg['To']一致
            smtp.quit()
            print('Email send success!')
        except Exception as e:
            print('Email send error!')
            raise e


if __name__ == '__main__':
    SendEmail().send_email()