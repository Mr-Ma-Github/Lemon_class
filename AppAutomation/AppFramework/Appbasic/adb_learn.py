#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-06-21 22:59

# 1.何为adb?
# adb (Android Debug Bridge)是android sdk的一个工具
# adb是用来连接安卓手机和PC端的桥梁,要有adb作为二者之间的维系,才能让
# 用户在电脑上对手机进行全面的操作。
# Android的初衷是用adb这样的一个工具来协助开发人员在开发android应用的过
# 程中更快更好的调试apk,因此adb具有安装卸载apk、拷贝推送文件、查看设备
# 硬件信息、查看应用程序占用资源、在设备执行shell命令等功能

# 2.adb常见命令
# adb --help 查看帮助手册
# adb devices 检测连接到电脑的安卓设备,这个是我们会经常用到的检测命令。
# adb logcat 打印log信息
# adb pull <手机路径> <本机路径>从手机中拉取信息放到本地电脑上
# adb push <本机路径> <手机路径>从本地推送信息到手机上去
# adb shell 登录设备shell(命令行的人机界面),ll ls命令都可以用,进入到linux命令环境
# 了,相当于执行远程命令!
# adb logcat--打印日志
# adb install xxx.apk 为了获取apk的安装包所在地址,可以直接把apk拖到cmd 的窗口获取
# 返回success就说明安装成功了!
# adb uninstall com.tencent.mobileqq---应用包名
# adb shell dumpsys activity | find "mFocusedActivity" ---查看前台应用activity名
# adb connect/disconnect 通过wifi进行远程连接手机进行调试
# adb kill-server--终止adb服务
# adb start-server-启动adb服务。通常在adb遇到问题时,与 adb kill-server一起使用。
# adb shell pm list packages ---列出所有包名
# 列出所有apk路径及包名
# -f列出所有apk路径及包名
# -s列出系统apk路径及包名
# -3列出用户apk路径及包名

# UI Automator
# UI自动化测试框架,安卓移动端app
# 要求: Android4.3以上
# 提供了一系列API:执行UI测试在系统或者第三方app上面
# 允许在被测设备上执行操作,比如打开系统设置菜单
# 适合编写黑盒自动化测试
# UI Automator框架的主要特点:
# 1、元素定位: UI Automator Viewer扫描、分析待测应用的U组件的图像工具
# 2、元素操作: Accessing device state,在目标设备和app上的各种操作
# 3、元素识别: UI Automator APls.在多个应用程序中捕获和操作UI组件
# https://developer.android.com/training/testing/ui-automator.html#ui-automator-viewer
def sum(a):
    a = a+1
    print(a)



c=sum(1)
print(c)

def changeNum(num) :
  num += 1
  print("自定义函数中的num = ",num)

#定义变量num，赋初始值为10
num = 10
#
changeNum(num)
print("函数调用后num = ",num)