import datetime
import base64
import hashlib
import requests
import json
from django.conf import settings

class YunTongXin():
    BASE_URL="https://app.cloopen.com:8883"
    def __init__(self,accountSid,auth_token,appId,templateId):
        self.accountSid=accountSid
        self.auth_token=auth_token
        self.appId=appId
        self.templateId=templateId
    def get_url(self,sig):
        url="/2013-12-26/Accounts/%s/SMS/TemplateSMS?sig=%s"%(self.accountSid,sig)
        post_url=self.BASE_URL+url
        return post_url
    def get_date(self):
        now_date=datetime.datetime.now()
        sj_date=now_date.strftime("%Y%m%d%H%M%S")
        return sj_date
    def get_sign(self,date):
        sig=self.accountSid+self.auth_token+date
        md5=hashlib.md5()
        md5.update(sig.encode())
        return md5.hexdigest().upper()
    #构造请求头
    def get_header(self,date):
        #作为一个参数的返回值，我们希望是一个字符串，而不是字节串
        token=self.accountSid + ":" + date
        bs_token=base64.b64encode(token.encode()).decode()
        header={"Accept":"application/json","Content-Type":"application/json;charset=utf-8","Authorization":bs_token}
        return header
    #构造请求体
    def get_body(self,phone,code):
        body={"to":phone,"appId":self.appId,"templateId":self.templateId,"datas":[code,3]}
        return body
    # 发送请求
    def send_request(self,url,header,body):
        res=requests.post(url,headers=header,data=json.dumps(body))
        return res.text
    # 完成发送请求
    def run(self,phone,code):
        my_date=self.get_date()
        sig=self.get_sign(my_date)
        url=self.get_url(sig)
        request_header=self.get_header(my_date)
        request_body=self.get_body(phone,code)
        return self.send_request(url,request_header,request_body)

if __name__ == '__main__':
    AUTH_TOKEN = "a36d8b9c2c0f4e84a2767ed091b98cee"
    ACCOUNT_SID = "8aaf07087c355e9b017c504ab14202eb"
    App_ID = "8aaf07087c355e9b017c504ab24f02f2"
    ytx=YunTongXin(ACCOUNT_SID,AUTH_TOKEN,App_ID,"1")
    res=ytx.run("15546328785","2221")
    print(res)


