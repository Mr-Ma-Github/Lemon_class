#-*-coding:utf-8-*-
#@作者：haiyu.ma
#@创建日期：2020-08-11 14:26 
import requests

url = "http://clinical-portal-snapshot.gene-go.com/api/orders?page=0&size=20&sort=id,desc&projectType=&Authorization=Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJoYWl5dS5tYSIsImF1dGgiOiJST0xFX09SREVSX1IsUk9MRV9BRE1JTixST0xFX1VTRVIiLCJleHAiOjE1OTcyMTI0MjB9.K8XyM6nLjeEjsLF0e7PZeGFHOQqaKVAxzWe-o5bRsMOe-B4cILQ6w7fH2yR_qt64jsbYTugEtnqpSTJsCMcQOw"

payload = {}
headers = {
  'Accept': 'application/json, text/plain, */*',
  'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJoYWl5dS5tYSIsImF1dGgiOiJST0xFX09SREVSX1IsUk9MRV9BRE1JTixST0xFX1VTRVIiLCJleHAiOjE1OTcyMTI0MjB9.K8XyM6nLjeEjsLF0e7PZeGFHOQqaKVAxzWe-o5bRsMOe-B4cILQ6w7fH2yR_qt64jsbYTugEtnqpSTJsCMcQOw'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text)
# print(response.text, type(response.text))

