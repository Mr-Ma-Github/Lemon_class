"""
============================
Author:柠檬班-木森
Time:2019/12/18
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

import time
from common.handle_sign import HandleSign

# 获取时间戳
timestamp = int(time.time())

# token值
token = "eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjI2NSwiZXhwIjoxNTc0NjY3MjMzfQ.ftrNcidmk_zxwl0" \
        "wzdhE5_39bsGlILoSSoTCy043fjhbjhCFG4FwCnOj4iy5svbDlSbgCJM3qRa1zsXJLJmH4A"

# 使用时间戳和token生成签名 sign
s = token[:50] +str(timestamp)


sign = HandleSign.to_encrypt(s)

data= {"aaa":111}
data2 = {
    "timestamp":timestamp,
    "sign":sign
}
# print(data2)
data.update(data2)


print(data)
