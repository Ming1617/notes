import requests
from useragents import ua_list
import time
import random
import re
import os
from urllib import parse

class BaiduImageSpider(object):
    def __init__(self):
        self.url='https://image.baidu.com/search/index?tn=baiduimage&word={}'
        #计数
        self.i=1

    #获取图片
    def get_image(self,url,word):
        headers={'User-Agent':random.choice(ua_list)}
        #1.获取图片链接列表
        res = requests.get(url=url, headers=headers)
        print(url)
        # 1.encoding 字符编码
        res.encoding = 'utf-8'
        # 2.text：响应内容-字符串
        html = res.text
        print(html)
        pattern=re.compile('"middleURL":"(.*?)"',re.S)
        img_link_list=pattern.findall(html)
        print(img_link_list)
        #创建对应的文件夹，用来保存图片
        # G://baidu//赵丽颖
        directory = 'G://baidu//{}//'.format(word)
        # 如果电影名路径不存在则先创建
        if not os.path.exists(directory):
            os.makedirs(directory)
        #2.for循环遍历，下载每张图片
        for img_link in img_link_list:
            self.save_image(img_link,directory,word)
            #休眠，控制爬取速度
            time.sleep(random.randint(1,2))

    #保存图片函数
    def save_image(self,img_link,directory,word):
        headers = {'User-Agent': random.choice(ua_list)}
        #1.向图片链接发请求，得到bytes类型
        html=requests.get(url=img_link,headers=headers).content
        filename=directory+'{}_{}.jpg'.format(word,self.i)
        #2.命名文件名，wb方式保存图片
        with open(filename,'wb')as f:
            f.write(html)
        self.i+=1
        print(filename,'下载成功')

    #入口函数
    def run(self):
        word=input('你想要谁的图片：')
        word=parse.quote(word)
        url=self.url.format(word)
        self.get_image(url,word)

if __name__=='__main__':
    spi=BaiduImageSpider()
    spi.run()