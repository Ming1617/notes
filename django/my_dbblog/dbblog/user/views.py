from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from django.views import View
from .models import user_list
import json
import re
import hashlib
from btoken.views import make_token
# Create your views here.
from tools.login_yz import login_check
from tools.SMS import YunTongXin
from django.utils.decorators import method_decorator
from django.conf import settings
import random
from django.core.cache import cache
class UsersView(View):
    def get(self,request,username=None):
        print(username)
        if username:
            try:
                user_obj=user_list.objects.get(username=username)
            except Exception as e:
                result={"code":1002,"error":"用户未登录"}
                return JsonResponse(result)
            if request.GET.keys():
                data={}
                for k in request.GET.keys():
                    if k=="password":
                        continue
                    if hasattr(user_obj,k):
                        data[k]=getattr(user_obj,k)
                result={"code":200,"username":username,"data":data}
                return JsonResponse(result)
            else:
                result={"code":200,"username":username,"data":{"nickname":user_obj.nickname,"info":user_obj.info,"avatar":str(user_obj.avatar),"sign":user_obj.sign}}
                return JsonResponse(result)
        return HttpResponse("ALL USERS")
    def post(self,request):
        json_str=request.body
        json_obj=json.loads(json_str)
        username=json_obj['username']
        password_1=json_obj['password_1']
        password_2=json_obj['password_2']
        email=json_obj['email']
        sms_num=json_obj['sms_num']
        phone=json_obj['phone']
        if len(phone)!=11:
            result={"code":4000,"error":"请检查手机号"}
            return JsonResponse(result)
        if not re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$',email):
            result={"code":40001,"error":"请检查邮箱格式"}
            return JsonResponse(result)
        if password_1!=password_2:
            result={"code":40001,"error":"两次密码不一致"}
            return JsonResponse(result)
        db_user=user_list.objects.filter(username=username)
        if db_user:
            result={"code":2123,"error":"用户名已经存在"}
            return JsonResponse(result)
        md5=hashlib.md5()
        md5.update(password_1.encode())
        password_hs=md5.hexdigest()
        try:
            user=user_list.objects.create(username=username,password=password_hs,email=email,phone=phone,nickname=username)
        except Exception as e:
            print("error:%s"%e)
            result={"code":444,"error":"您慢了一步，刚刚被人注册了"}
            return JsonResponse(result)
        # 签发jwt
        token=make_token(username)
        return JsonResponse({"code":200,"username":username,"data":{"token":token.decode()}})
    @method_decorator(login_check)
    def put(self,request,username):
        json_str=request.body
        json_obj=json.loads(json_str)
        user_obj=request.my_user
        user_obj.nickname=json_obj["nickname"]
        user_obj.sign=json_obj["sign"]
        user_obj.info=json_obj["info"]
        user_obj.save()
        result={"code":200,"data":{"nickname":user_obj.nickname,"sign":user_obj.sign,"info":user_obj.sign}}
        return JsonResponse(result)


@login_check
def user_avatar(request,username):
    if request.method!="POST":
        result={"code":10001,"error":"只能用post方法提交"}
        return JsonResponse(result)

    #这种方法是从地址栏中获取的，通过path转换器拿到用户名
    # user_obj=user_list.objects.get(username=username)

    user_obj=request.my_user
    user_obj.avatar=request.FILES["avatar"]
    user_obj.save()
    result={"code":200,'username':username}
    return JsonResponse(result)

def send_sms(request):
    json_str=request.body
    json_obj=json.loads(json_str)
    phone=json_obj["phone"]
    #防止用户重复获取验证码
    cache_key="sms_%s"%phone
    old_cache_key=cache.get(cache_key)
    if old_cache_key:
        return JsonResponse({"code":2000002,"error":"请不要重复获取验证码"})
    code = get_random_code()
    ytx=YunTongXin(settings.ACCOUNT_SID,settings.AUTH_TOKEN,settings.APP_ID,settings.TEMPLATE_ID)
    res=ytx.run(phone,code)
    cache.set(cache_key,code,65)
    print(res)
    return JsonResponse({"code":200})

def get_random_code():
    code=random.randint(10000,50000)
    return code