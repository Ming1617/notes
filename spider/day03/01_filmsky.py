'''
电影天堂案例抓取
'''
from urllib import request
from useragents import ua_list
import time
import random
import re


class FilmSky(object):
    def __init__(self):
        self.url='https://www.ygdy8.com/html/gndy/dyzz/list_23_{}.html'

    #请求函数
    def get_html(self,url):
        headers={'User-Agent':random.choice(ua_list)}
        req=request.Request(url=url,headers=headers)
        res=request.urlopen(req)
        #1.查看网页源码，查看网站的编码
        #2.decode（）第二个参数：ignore 忽略掉特殊字符
        html=res.read().decode('gb2312','ignore')

        return html

    #正则解析函数
    def re_func(self,re_bds,html):
        pattern=re.compile(re_bds,re.S)
        r_list=pattern.findall(html)

        return r_list

    #解析：一级页面  - 详情页的链接
    def parse_html(self,one_url):
        one_html=self.get_html(one_url)
        re_bds='<table width="100%".*?<td width="5%".*?<a href="(.*?)".*?ulink">.*?</table>'
        #one_list:['/html/xxx/xxx','','']
        one_list=self.re_func(re_bds,one_html)
        for href in one_list:
            two_url='https://www.ygdy8.com'+href
            # 在此，获取到此电影所有数据，然后再遍历下一个
            self.get_film_info(two_url)
            #随机休眠
            time.sleep(random.randint(1,2))


    #解析二级页面：电影详情页函数*没有下载链接
    def get_film_info(self,two_url):
        item={}
        two_html=self.get_html(two_url)
        re_bds='<div class="title_all"><h1><font color=#07519a>(.*?)</font></h1>'
        #film_list:['x战警']
        film_list=self.re_func(re_bds,two_html)
        #电影名称
        item['name']=film_list[0].strip()
        print(item)

    #入口函数
    def run(self):
        for page in range(1,201):
            url=self.url.format(page)
            self.parse_html(url)

if __name__=='__main__':
    spider=FilmSky()
    spider.run()

