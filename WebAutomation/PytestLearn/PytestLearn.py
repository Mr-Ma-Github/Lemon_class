#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-06-04 22:05

# pytest
# Pytest:基于unittest之上的单元测试框架。
# 1、自动发现测试模块和测试方法;
# 2、断言使用assert +表达式即可:
# 3、可以设置会话级、模块级、类级、函数级的fixtures 数据准备+清理工作
# 4、有丰富的插件库,目前在300个以上。= allure

# 安装命令:
# pip install pytest
# 安装html报告的插件:
# pip install pytest-html
#
# Pytest插件地址:
# http://plugincompat.herokuapp.com/

# pytest - 收集测试用例
# pytest收集测试用例的规则:
# 1、默认从当前目录中搜集测试用例,即在哪个目录下运行pytest命令,则从哪个目录当中搜索:
# 2、搜索规则:
# 1)符合命名规则 test_*.py 或者 *_test.py 的文件
# 2) 以test_开头的函数名:
# 3) 以Test开头的测试类(没有_init_函数)当中,以test_开头的函数

# pytest - mark
# 对测试用例打标签。在运行测试用例的时候,可根据标签名来过滤要运行的用例。
# 使用方法:
# 在测试用例/测试类前面加上:@pytest.mark.标记名
# 示例:
# @pytest.mark.smoke
# 可在一个用例上打多个标签。多次使用@pytest.mark.标签名即可。
# 示例:
# @pytest.mark.smoke
# @pytest.mark.demo
# def test_demo():
#     print("我是示例例啦!!!")
# 运行：输出台下方-Terminal，pytest -m smoke

# pytest - 定义fixture
# fixture:即测试用例执行的环境准备和清理,在unittest中即指setup/teardown/setupClass/teardownClass
# fixture主要的目的是为了提供一种可靠和可重复性的手段去运行那些最基本的测试内容。
# 比如在测试网站的功能时,每个测试用例都要登录和退出,利用fixture就可以只做一次,否则每个测试用例都要做这两步
# 定义fixture:
# 把一个函数定义为Fixture很简单,在函数声明之前加上@pytest.fixture。
# 表示此函数为测试环境数据的准备和清理。
# 那么在一个fixture内部如何区分环境准备、环境清理呢?
# 在函数内使用yield关键字
# yield关键字以后的代码,就是环境清理的代码,即在测试用例执行完成之后会执行的代码。
# fixture返回值
# fixture定义之后的使用

# pytest - 参数化
# 在测试用例的前面加上:
# @pytest.mark.parametrize("参数名",列表数据)
# 参数名:用来接收每一项数据,并作为测试用例的参数。
# 列表数据:一组测试数据。

# pytest-重运行机制
# Pytest提供了失败重试机制:
# 4ZE: rerunfailures
# pip install pytest-rerunfailures
# 使用方式:
# 命令行参数形式:
# 命令:pytest --reruns 重试次数
# 比如:pytest --reruns 2 表示:运行失败的用例可以重新运行2次。
# 命令:pytest --reruns 重试次数 --reruns-delay 次数之间的延时设置(单位:秒)
# Pytest --reruns 2 --reruns-delay 5
# 表示失败的用例可以重新运行2次。第一次和第二次的间隔时间为5秒钟

# 优化 - pytest - html
# 需要安装pytest - html插件。
# Pytest可以生成多种样式的结果:
# 1. 生成JunitXML 格式的测试报告:命令:--junitxml = path
# 2. 生成result log格式的测试报告:命令:--resultlog=report\log.txt
# 3. 生成Html格式的测试报告:命令:--html=report\test_one_func.html
# pytest -m demo --reruns 2 --reruns-delay 5 -s --junitxml=Outputs/reports/report.xml --html=Outputs/reports/html_report.html --alluredir=Outputs/allure_reports

# pytest - allure报告
# 1、安装allure
#    1) 下载 allure.zip
#    下载地址: allure-github: https://github.com/allure-framework/allure2
#    2) 解压到本地目录、配置allure.bat的环境变量ALLURE_HOME;
#    在命令行中运行allure.确认环镜变量配置成功。
#    环境变量：ALLURE_HOME      文件安装路径(bin)例如：D\allure-2.7.0\bin
# 2、pytest插件安装     命令: pip install pytest-allure-adaptor
# 3、Pytest生成allure测试报告的命令参数   命令:--alluredir=/XXX/my_allure_results
# 4、查看allure的测试报告  命令：allure serve allure 报告目录
# 示例: allure serve D:\python_web_pytest_allure\HtmlTestReport\allure
# allure文档: https://docs.qameta.io/allure/
