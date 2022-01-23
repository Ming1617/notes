'''
向测试网站：http://httpbin.org/get 发请求，从响应内容中确认User-Agent
'''
from urllib import  request
res=request.urlopen(url='http://httpbin.org/get')
html=res.read().decode()
print(html)