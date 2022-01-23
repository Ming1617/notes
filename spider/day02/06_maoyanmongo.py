from urllib import request
import re
import time
import random
from useragents import ua_list
import pymongo

class MaoyanSpider(object):
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'
        # 3个对象
        self.conn = pymongo.MongoClient(
            'localhost',27017
        )
        self.db = self.conn['maoyandb']
        self.myset = self.db['maoyanset']

    def get_html(self,url):
        headers = {'User-Agent':random.choice(ua_list)}
        req = request.Request(url=url,headers=headers)
        res = request.urlopen(req)
        html = res.read().decode()
        # 直接解析
        self.parse_html(html)

    def parse_html(self,html):
        re_bds = '<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?class="releasetime">(.*?)</p>'
        pattern = re.compile(re_bds,re.S)
        # r_list: [('大话西游','周星驰','1994'),(),()]
        r_list = pattern.findall(html)
        self.save_html(r_list)

    # mongodb数据库: maoyandb -> maoyanset
    def save_html(self, r_list):
        for r in r_list:
            # item定义在for循环里边
            item = {}
            item['name'] = r[0].strip()
            item['star'] = r[1].strip()[3:]
            item['time'] = r[2].strip()[5:15]
            print(item)
            self.myset.insert_one(item)
            # insert_many([{},{},{},{}])

    def run(self):
        for offset in range(0,31,10):
            url = self.url.format(offset)
            self.get_html(url)
            time.sleep(random.uniform(1,2))


if __name__ == '__main__':
    spider = MaoyanSpider()
    spider.run()

































