from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from django.views import View
import json
from user.models import user_list
import hashlib
from django.conf import settings
import time
import jwt
# Create your views here.


class BtokenViews(View):
    def get(self,request):
        return HttpResponse("get token")
    def post(self,request):
        json_str=request.body
        json_obj=json.loads(json_str)
        username=json_obj["username"]
        password=json_obj["password"]
        try:
            user_obj=user_list.objects.get(username=username)
            if not user_obj:
                return JsonResponse({"code":200,"error":"用户名或密码错误"})
        except Exception as e:
            result={"code":3000,"error":"用户名或密码错误"}
            return JsonResponse(result)
        md5 = hashlib.md5()
        md5.update(password.encode())
        new_password_hs = md5.hexdigest()
        db_password = user_obj.password
        if new_password_hs != db_password:
            result = {"code": 40001, "error": "用户名或密码错误"}
            return JsonResponse(result)
        token = make_token(username)
        return JsonResponse({"code": 200, "username": username,"data": {"token": token.decode()}})  # jsonresponse传递的是字符串，因为底层会自动转换为字节串传递


def make_token(username,expire=3600*24):
    payload={"username":username,"exp":expire+time.time()}
    key=settings.JWT_TOKEN_KEY
    token=jwt.encode(payload,key,algorithm="HS256")
    return token