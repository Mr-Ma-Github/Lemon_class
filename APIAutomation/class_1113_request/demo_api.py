#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-08-26 22:53

# pip install flask
from flask import Flask

app = Flask(__name__)

@app.route("/login", methods=['GET', 'POST']) #接口地址  @ 装饰器
def login():
    return "你已经登录成功", 200

# login()
# /login地址和 login函数绑定在一起
# 访问/login地址的时候函数会被调用

if __name__ == "__main__":
    app.run()
    # http://localhost:5000/login