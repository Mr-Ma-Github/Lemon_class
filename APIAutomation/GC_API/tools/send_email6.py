# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2019-12-26 16:58
# coding: utf-8
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from GC_API.tools.case_config import ReadConfig
from GC_API.tools import project_path


class SendEmail:
    # 设置smtplib所需的参数
    smtp_config = eval(ReadConfig.get_config(project_path.case_config_path, 'EMAIL', 'smtp_config'))
    def send_email(self, report_path=None):
        # 构造邮件对象MIMEMultipart对象
        msg = MIMEMultipart('mixed')
        msg['Subject'] = '自动化测试报告'  # 邮件主题
        msg['From'] = self.smtp_config["sender"]  # 发送方信息
        msg['To'] = ",".join(self.smtp_config["receivers"])  # 接收方信息

        # 构造文字内容
        text = "Hello!\nThis is a Interface automation test report!"
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
            smtp.connect(self.smtp_config["host"], 25)
            # 我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
            # smtp.set_debuglevel(1)
            smtp.login(self.smtp_config["sender"], self.smtp_config["password"])
            smtp.sendmail(self.smtp_config["sender"], self.smtp_config["receivers"], msg.as_string())
            smtp.quit()
            print('Email send success!')
        except Exception as e:
            print('Email send error!')
            raise e


if __name__ == '__main__':
    SendEmail().send_email()