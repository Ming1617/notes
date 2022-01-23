from django.http import JsonResponse
from user.models import user_list
from django.conf import settings
import jwt
def login_check(func):
    def warp(request,*args,**kwargs):
        token=request.META.get("HTTP_AUTHORIZATION")
        if not token:
            result={"code":10009,"error":"用户未登录，请登录"}
            return JsonResponse(result)
        try:
            res=jwt.decode(token,settings.JWT_TOKEN_KEY,algorithms="HS256")
        except Exception as e:
            print("error is %s"%e)
            result={"code":"10001","error":"用户未登录"}
            return JsonResponse(result)
        username=res["username"]
        user_obj=user_list.objects.get(username=username)
        request.my_user=user_obj
        return func(request,*args,**kwargs)
    return warp

