"""
猫眼电影抓取存入mysql数据库
"""
import re
from urllib import request
import time
import random
from  useragents import ua_list
import pymysql

class MaoyanSpider(object):
    def __init__(self):
        self.url='https://maoyan.com/board/4?offset={}'
        self.i=0
        # 连接数据库
        self.db = pymysql.connect(host="localhost",
                             port=3306,
                             user='root',
                             password='010113',
                             database='maoyandb',
                             charset='utf8')
        #创建游标对象
        self.cur = self.db.cursor()

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
        re_bds='<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?class="releasetime">(.*?)</p>'
        pattern=re.compile(re_bds,re.S)
        r_list=pattern.findall(html)

        self.write_html(r_list)

    #保存 利用executemany
    def write_html(self, r_list):
        L = []
        ins = 'insert into filmtab values(%s,%s,%s)'
        for r in r_list:
            t = [
                r[0].strip(), r[1].strip(), r[2].strip()[5:15]
            ]
            L.append(t)
            self.i+=1

        self.cur.executemany(ins, L)
        # 提交到数据库执行
        self.db.commit()


    # #保存利用execute
    # def write_html(self,r_list):
    #     ins='insert into filmtab values(%s,%s,%s)'
    #     for r in r_list:
    #         L=[
    #             r[0].strip(),r[1].strip(),r[2].strip()[5:15]
    #         ]
    #         self.i+=1
    #         self.cur.execute(ins,L)
    #         #提交到数据库执行
    #         self.db.commit()


    #主函数
    def run(self):
        for offset in range(0,101,10):
            url=self.url.format(offset)
            self.get_html(url)
            # 随机休眠时间 - uniform生成随机浮点数
            time.sleep(random.uniform(1,5))
        print('数量：', self.i)
        # 关闭数据库对象游标对象
        self.cur.close()
        self.db.close()

if __name__=='__main__':
    start=time.time()
    spider=MaoyanSpider()
    spider.run()
    end=time.time()
    print('执行时间：%.2f'%(end-start))