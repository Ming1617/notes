"""
向百度发起请求，并获取百度的响应内容
"""
from urllib import  request

res=request.urlopen(url='http://www.baidu.com')
#响应对象方法1:read() ->  bytes 需要转码
html=res.read().decode()
# print(html)
#响应方法2：geturl() -> 返回实际数据
url=res.geturl()
# print(url)
#响应对象方法3：getcode() -> 返回HTTP响应状态码
code=res.getcode()
print(code)

