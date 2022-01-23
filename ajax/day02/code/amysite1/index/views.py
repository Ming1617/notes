import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import User
# Create your views here.
def xhr_view(request):

    return render(request, 'index/xhr.html')

def xhr_get(request):

    return render(request, 'index/xhr_get.html')

def xhr_get_server(request):
    if request.GET.get('params'):
        p = request.GET['params']
        return HttpResponse('%s is received'%(p))
    return HttpResponse('This is ajax !')

def register(request):

    if request.method == 'GET':
        return render(request,  'index/register.html')
    elif request.method == 'POST':
        username = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        try:
            User.objects.create(username=username, pwd=pwd, nickname=username)
        except Exception as e:
            print('register error is %s'%(e))
            return HttpResponse('--用户名已注册--')
        return HttpResponse('--注册成功--')


def get_user(request):
    #拿页面
    return render(request, 'index/get_user.html')

def get_user_server(request):
    #拿数据 返回结构自定义
    # all_user = User.objects.all()
    # msg = ''
    # for u in all_user:
    #     msg += '%s_%s_%s|'%(u.id, u.username, u.pwd)
    # last_msg = msg[0:-1]

    #拿数据 json版本
    d = []
    all_user = User.objects.all()
    for u in all_user:
        d.append({'id':u.id, 'username':u.username, 'pwd':u.pwd})
    json_str = json.dumps(d)
    return HttpResponse(json_str, content_type='application/json')


def test_json(request):

    return render(request, 'index/test_json.html')

def json_dumps(request):

    # 1 json序列化  python-obj -> json串
    # 2 json反序列化 json串 -> Python-obj

    #序列化单个对象
    # dic = {
    #     'name' : 'wanglaoshi',
    #     'age': 18
    # }

    # json_str = json.dumps(dic)
    # return HttpResponse(json_str)

    #序列化多个对象
    # s = [
    #     {
    #         'name': 'guo',
    #         'age': 18
    #     },
    #     {
    #         'name': 'wang',
    #         'age': 19
    #     }
    # ]
    # json_str = json.dumps(s)
    # return HttpResponse(json_str)

    # all_user = User.objects.all()
    # d = []
    # for u in all_user:
    #     d.append({'name':u.username})
    # return HttpResponse(json.dumps(d))

    #django v1 serializers
    # from django.core import serializers
    # all_user = User.objects.all()
    # json_str = serializers.serialize('json',all_user)
    # return HttpResponse(json_str)

    #django v2
    d = []
    all_user = User.objects.all()
    for u in all_user:
        d.append({'name':u.username})
    #JsonResponse(dict)
    #{'code':1000, 'data':{}}
    #return JsonResponse({'all_user':d})

    return HttpResponse(json.dumps(d),content_type='application/json')





















































def check_username(request):
    #检查用户名
    username = request.GET.get('username')
    #filter
    users = User.objects.filter(username=username)
    if users:
        #1 代表用户名已存在
        return HttpResponse('1')
    #0 代表 用户名可用
    return HttpResponse('0')


def xhr_post(request):

    return render(request, 'index/xhr_post.html')

def xhr_post_server(request):

    username = request.POST.get('username','')
    print('my username is %s'%(username))
    return HttpResponse('post is ok')






























