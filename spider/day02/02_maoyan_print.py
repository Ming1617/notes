import re
from urllib import request
import time
import random
from  useragents import ua_list
import csv

class MaoyanSpider(object):
    def __init__(self):
        self.url='https://maoyan.com/board/4?offset={}'
        self.i=0

    #请求
    def get_html(self,url):
        headers={'User-Agent':random.choice(ua_list)}
        req=request.Request(url=url,headers=headers)
        res=request.urlopen(req)
        html=res.read().decode()

        self.parse_html(html)


    #解析
    def parse_html(self,html):
        #r_list:[('月光宝盒','周星驰','1994-01-01'),(),()....]
        re_bds='<div class="movie-item-info">.*?title="(.*?)".*?class="star">(.*?)</p>.*?releasetime">(.*?)</p>'
        pattern=re.compile(re_bds,re.S)
        r_list=pattern.findall(html)

        self.write_html(r_list)


    #保存
    def write_html(self,r_list):
        item={}
        #以 a 方式打开文件,如果w则只保留最后一页数据
        with open('maoyan.csv','a',encoding='utf-8',newline='') as f:
            writer=csv.writer(f)
            for r in r_list:
                item['name']=r[0].strip()
                item['star']=r[1].strip()
                item['time']=r[2].strip()[5:15]
                print(item)
                L=[item['name'],item['star'],item['time']]
                writer.writerow(L)
                self.i+=1

    #主函数
    def run(self):
        for offset in range(0,101,10):
            url=self.url.format(offset)
            self.get_html(url)
            # 随机休眠时间 - uniform生成随机浮点数
            time.sleep(random.uniform(1,2))
        print('数量：', self.i)

if __name__=='__main__':
    start=time.time()
    spider=MaoyanSpider()
    spider.run()
    end=time.time()
    print('执行时间：%.2f'%(end-start))