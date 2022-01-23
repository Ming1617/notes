from urllib import request
import os

directory = '/home/tarena/images/霸王别姬/'
if not os.path.exists(directory):
    os.makedirs(directory)

url = 'https://p1.meituan.net/movie/2e9a54816057aebd2f05fce7e93600ac75013.jpg@465w_258h_1e_1c'
headers = {'User-Agent':'Mozilla/5.0'}

req = request.Request(url=url,headers=headers)
res = request.urlopen(req)
html = res.read()

# filename: /home/tarena/images/霸王别姬/xxx.jpg
filename = directory + url.split('@')[0][-10:]
# 保存图片
with open(filename,'wb') as f:
    f.write(html)

# /home/tarena/images/霸王别姬/xxx.jpg







