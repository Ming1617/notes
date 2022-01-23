import requests

url='http://www.baidu.com/'
headers={'User-Agent':'Mozilla/5.0'}
res=requests.get(url=url,headers=headers)
#1.encoding 字符编码
res.encoding='utf-8'
#2.text：响应内容-字符串
html=res.text
print(html)
#3.content: 响应内容-字节串
html=res.content
#4.status_code ：HTTP响应码
code=res.status_code
#5.url ：实际数据的URL地址
real_url=res.url
print(code,real_url)
# print(html)