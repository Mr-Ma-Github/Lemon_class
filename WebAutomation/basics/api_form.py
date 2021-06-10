# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2021-03-25 14:47
# @Software：PyCharm
# ----------------------------------------------------------------------------
# import requests
#
# url = "http://clinical-portal-snapshot.gene-go.com/api/static/file-create?folderPath=orders/"
# # webform
# files = {'file': ("Lighthouse.jpg", open('D:/Lighthouse.jpg', "rb"), "image/jpg")}
#
# header = {
#     "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
#     # 'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryk95Gu2v20sOlwcO0',
#     'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJoYWl5dS5tYSIsImF1dGgiOiJST0xFX09SREVSX1IsUk9MRV9BRE1JTixST0xFX1VTRVIiLCJleHAiOjE2MTY3NDA0NzB9.Fg9rm7S-OQcNdsT72onODwOkJFkZ_BWH_iO-xjYZ-WC9pc2TWXV86HQkb2wr2wijyoZo6XN1CIQlzAHHdDf_RQ'
# }
#
# #使用requests 的post方法提交数据
# res = requests.post(url, files=files, headers=header)
# print(res.text)


# 封装：
import requests
import os
url = "http://clinical-portal-snapshot.gene-go.com/api/static/file-create?folderPath=orders/"

def upload_file(url, file_name, file_path='/root/image'):
    _file = os.path.join(file_path, file_name)
    files = {'file': (file_name, open(_file, "rb"), "image/jpg")}
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
              # 'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryk95Gu2v20sOlwcO0',
              'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJoYWl5dS5tYSIsImF1dGgiOiJST0xFX09SREVSX1IsUk9MRV9BRE1JTixST0xFX1VTRVIiLCJleHAiOjE2MTY3NDA0NzB9.Fg9rm7S-OQcNdsT72onODwOkJFkZ_BWH_iO-xjYZ-WC9pc2TWXV86HQkb2wr2wijyoZo6XN1CIQlzAHHdDf_RQ'}
    try:
        #使用requests 的post方法提交数据
        res = requests.post(url, files=files, headers=header)
        print(res.text)
        return res.text
    except:
        print("请求有问题!请检查代码")

if __name__ == '__main__':
    file_name = 'Lighthouse.jpg'
    file_path = "D:/"  # /root/image
    # _file = os.path.join(file_path, file_name)
    # print(_file)
    upload_file(url,file_name, file_path)