# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2019-12-26 16:58
# coding: utf-8

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header

# 设置smtplib所需的参数
host = 'smtp.163.com'  # 163邮箱服务器地址
password = 'TGZJUHKFOLKWQBBT'  # 密码(部分邮箱为授权码)
sender = '15083158852@163.com'  # 邮件发送方邮箱地址
receivers = ['haiyu.ma@genomicarebio.com']  # 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发

# 构造邮件对象MIMEMultipart对象
msg = MIMEMultipart('mixed')
msg['Subject'] = '自动化测试报告'  # 邮件主题
msg['From'] = sender  # 发送方信息
# msg['To'] = 'XXX@126.com'
# 收件人为多个收件人,通过join将列表转换为以,为间隔的字符串
msg['To'] = ",".join(receivers)

# 构造文字内容
text = "Hello!\nThis is a Interface automation test report!"
text_plain = MIMEText(text, 'plain', 'utf-8')
msg.attach(text_plain)

# 构造图片
sendimagefile = open(r'D:\Lighthouse.jpg', 'rb').read()
image = MIMEImage(sendimagefile)
image.add_header('Content-ID', '<image1>')
image["Content-Disposition"] = 'attachment; filename="testimage.png"'
msg.attach(image)

# # 构造html
# # 发送正文中的图片:由于包含未被许可的信息，网易邮箱定义为垃圾邮件，报554 DT:SPM ：<p><img src="cid:image1"></p>
# html = """
# <html>
#   <head></head>
#   <body>
#     <p>Hi!<br>
#        How are you?<br>
#        Here is the <a href="http://www.baidu.com">link</a> you wanted.<br>
#     </p>
#   </body>
# </html>
# """
# text_html = MIMEText(html, 'html', 'utf-8')
# text_html["Content-Disposition"] = 'attachment; filename="texthtml.html"'
# msg.attach(text_html)

# 构造附件
html_path = R'C:\Users\haiyu.ma\PycharmProjects\lemon_class\APIAutomation2021\GC_API\test_result\html_report\report20210413-2326.html'
sendfile = open(html_path, 'rb').read()
text_att = MIMEText(sendfile, 'base64', 'utf-8')
# 以下附件可以重命名成aaa.txt
# text_att["Content-Disposition"] = 'attachment; filename="aaa.txt"'
# 另一种实现方式
text_att.add_header('Content-Disposition', 'attachment', filename='test_report.html.')
msg.attach(text_att)

# 发送邮件
smtp = smtplib.SMTP()
smtp.connect(host, 25)
# 我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
smtp.set_debuglevel(1)
smtp.login(sender, password)
smtp.sendmail(sender, receivers, msg.as_string())
smtp.quit()

