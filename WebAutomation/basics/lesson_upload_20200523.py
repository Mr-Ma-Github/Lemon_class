#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-05-23 15:03
# 上传操作
# 有两种情况:
# 1、如果是input 可以直接输入路径的,那么直接调send_keys输入路径
# 2、非input标签的上传,则需要借助第三方工具:
# 1) Autolt 我们去调用其生成的au3或exe文件。
# 2) SendKeys第三方库 (目前只支持到2.7版本)
# 网址: https://pypi.python.org/pypi/SendKeys
# 3) Python pywin32库,识别对话框句柄,进而操作pyautoit
# 工具:
# Pywin32 和 py++
# 例:百度网盘-上传窗口
# ---------------------------------------------------------------------
# ！！结构模型：                      上传窗口
#                          win-32gui.FindWindow
#
#             子窗口打开按钮                子窗口--ComboBoxEx32
#      win32gui.FindWindowEx                win32gui.FindWindowEx
#
#                                           子窗口--ComboBox
#                                           win32gui.FindWindowEx
#
#                                           子窗口文件路径输入区域--Edit
#                                           win32gui.FindWindowEx
# --------------------------------------------------------------------------
# 上传操作
#chrome
import win32gui
import win32con
# 谷歌浏览器
def upload_file(filepath):
    dialog = win32gui.FindWindow("#32770","打开") # 一级窗口
    # 二级窗口
    ComboBoxEx32 = win32gui.FindWindowEx(dialog,0,"ComboBoxEx32",None)
    # 三级窗口
    comboBox = win32gui.FindWindowEx(ComboBoxEx32,0,"ComboBox",None)
    # 文本的输入窗口-四级
    edit = win32gui.FindWindowEx(comboBox,0,"Edit",None)
    # 打开按钮-四级
    button = win32gui.FindWindowEx(dialog,0,"Button","打开(&O)")
    # 输入文件地址
    win32gui.SendMessage(edit,win32con.WM_SETTEXT,None,filepath) # 发送文件路径
    # 点击打开按钮  提交文件
    win32gui.SendMessage(dialog,win32con.WM_COMMAND,1,button)


upload_file("C:\\Users\haiyu.ma\Pictures\dr.jpg")