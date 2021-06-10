#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-06-04 23:16 
import pytest
from selenium import webdriver
from PageObjects.login_page import LoginPage
from TestDatas import Common_Datas as CD

def pytest_configure(config):
    marker_list = ["demo","smoke","parametrize"]  # 标签名集合
    for markers in marker_list:
        config.addinivalue_line("markers", markers)

driver = None
# 声明它是一个fixture
@pytest.fixture(scope="class")
def access_web():
    global driver
    # 前置条件
    driver = webdriver.Chrome()
    driver.get(CD.web_login_url)
    lg = LoginPage(driver)
    yield(driver, lg)   #分隔线   # 后面接返回值--元祖
    # 后置条件
    driver.quit()

@pytest.fixture
def refresh_page():
    global driver
    # 前置条件
    yield
    # 后置条件
    driver.refresh()

@pytest.fixture(scope="session")
def session_demo():
    print("**********我是整个会话期间的开始*********")
    yield
    print("**********我是整个会话期间的结束*********")

@pytest.fixture(scope="class")
def class_demo():
    print("**********我是class的开始*********")
    yield
    print("**********我是class的结束*********")

@pytest.fixture
def func_demo():
    print("**********我是fuction的开始*********")
    yield
    print("**********我是fuction的结束*********")

# 运行测试用例有警告：Pytest Unknown Mark Warning: Unknown pytest.mark.demo - is this a typo?
# You can register custom marks to avoid this warning - for details,
# 警告的意思大概就是pytest不认得这个标记，导致标签不生效
# 解决方案：
# 1.单个标签
# 在conftest.py添加如下代码，直接拷贝过去，把标签名改成你自己的就行了
# def pytest_configure(config):
#     config.addinivalue_line(
#     "markers", "login_success") # login_success 是标签名
# 2.多个标签
# 在conftest.py添加如下代码，直接拷贝过去，把标签名改成你自己的就行了
# def pytest_configure(config):
#     marker_list = ["testmark1","testmark2","testmark3"]  # 标签名集合
#     for markers in marker_list:
#         config.addinivalue_line("markers", markers)
# 3.添加pytest.int 配置文件
# 这个方法单个标签和多个标签都适用
# [pytest]
# markers = testmark1
# testmark2
# testmark3'''