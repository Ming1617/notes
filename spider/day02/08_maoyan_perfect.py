import re
from  urllib import  request
from useragents import ua_list
import time
import random
import os

class  MaoyanSpider(object):
    def __init__(self):
        self.url='https://maoyan.com/board/4?offset={}'

    #功能函数1：获取响应内容
    def get_html(self,url):
        headers = {'User-Agent': random.choice(ua_list)}
        req = request.Request(url=url, headers=headers)
        res = request.urlopen(req)
        html = res.read()
        # print(html)
        return html

    #功能函数2：解析提取数据
    def re_func(self,re_bds,html):
        pattern=re.compile(re_bds,re.S)
        # print(html)
        r_list=pattern.findall(html)
        return r_list

    #获取想要的数据 - 解析1级页面
    def parse_html(self,url):
        one_html=self.get_html(url).decode()
        # print(one_html)
        re_bds='<div class="movie-item-info">.*?<a href="(.*?)".*?title="(.*?)".*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>'
        #one_list:[('html/590','霸王别姬','','')]
        one_list=self.re_func(re_bds,one_html)
        print(one_list)
        #直接调用数据处理函数
        self.write_html(one_list)

    def write_html(self,one_list):
        item={}
        for one in one_list:
            #one:一个电影信息,把所有事情搞定
            #电影名+主演+时间+评论+图片
            item['name']=one[1].strip()
            item['star']=one[2].strip()
            item['time']=one[3].strip()
            two_url='https://maoyan.com'+one[0]
            item['comment']=self.get_comment(two_url)
            print(item)
            #保存该电影所有图片
            self.save_image(two_url,item['name'])

    #从详情页中提取评论
    def get_comment(self,two_url):
        tow_html=self.get_html(two_url).decode()
        re_bds='<div class="comment-content">(.*?)</div>'
        comment_list=self.re_func(re_bds,tow_html)
        return comment_list


    #从详情页中提取出图片链接，并把图片保存到本地
    def save_image(self,two_url,name):
        #1.提取图片链接
        tow_html=self.get_html(two_url).decode()
        # print(tow_html)
        re_bds='<div class="img.*?"><img class="default-img" data-src="(.*?)" alt=".*?" /></div>'
        img_link_list=self.re_func(re_bds,tow_html)
        print(img_link_list)

        # /maoyan/top100/喜剧之王/
        directory='G://maoyan//top100//{}//'.format(name)
        #如果电影名路径不存在则先创建
        if not os.path.exists(directory):
            os.makedirs(directory)


        #2.保存图片:img_link:http://xxxx.jpg
        for img_link in img_link_list:
            img_html=self.get_html(img_link)
            #利用链接解决文件名问题：xxx.jpg
            #filename:/home/ming/maoyan/top/喜剧之王/xxx.jpg
            filename=directory+img_link.split('/')[-1].split('@')[0]
            with open(filename,'wb')as f:
                f.write(img_html)
            #每抓取一张图片
            time.sleep(random.randint(1,2))

    #入口函数
    def run(self):
        for offset in range(0,11,10):
            url=self.url.format(offset)
            print(url)
            self.parse_html(url)

            time.sleep(random.randint(1,3))

if __name__ =='__main__':
    spider=MaoyanSpider()
    spider.run()