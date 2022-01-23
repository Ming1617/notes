from urllib import request
import time
import random
from  useragents import ua_list
from lxml import etree

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
        parse_obj=etree.HTML(html)
        item={}
        #1.基准xpath
        dd_list=parse_obj.xpath('//dl[@class="board-wrapper"]/dd')
        #2.for循环遍历，以此获取每个电影信息
        for dd in dd_list:
            item['name']=dd.xpath('.//p[@class="name"]/a/text()')[0].strip()
            item['star']=dd.xpath('.//p[@class="star"]/text()')[0].strip()
            item['time']=dd.xpath('.//p[@class="releasetime"]/text()')[0].strip()
            print(item)


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