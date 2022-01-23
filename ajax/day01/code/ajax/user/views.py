import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from .models import User
def xhr(request):

    return render(request,'xhr.html')


def get_xhr(request):
    return render(request,'get_xhr.html')

def get_xhr_server(request):
    if request.GET.get('uname'):
        uname=request.GET['uname']
        return HttpResponse('welcome %s'%(uname))
    return HttpResponse('This is ajax')

def register(request):
    if request.method =='GET':
        return render(request,'register.html')
    elif request.method=='POST':
        #register
        uname=request.POST.get('uname')
        if not uname:
            return HttpResponse('请输入用户名')
        #查询 用户名
        pwd=request.POST.get('pwd')
        if not pwd:
            return HttpResponse('请输入密码')
        nickname=request.POST.get('nickname')
        if not nickname:
            return HttpResponse('请输入昵称')
        try:
            User.objects.create(uname=uname,pwd=pwd,nickname=nickname)

        except Exception as e:
            return HttpResponse('注册失败，请稍后重试！')
        return HttpResponse('注册成功')

def get_user(request):
    return render(request,'get_user.html')

def get_user_server(request):
    user=User.objects.all()
    msg=''
    for u in user:
        msg+= '%s_%s_%s|' %(u.uname,u.pwd,u.nickname)
    last_msg=msg[0:-1]
    return HttpResponse(last_msg)

def json_obj(request):

    return render(request,'json_obj.html')

def json_dumps(request):
    #1.生成单个对象的json字符串  序列化 -> obj - str
    #separators:参数（'，','：'）,地一个参数指的是没一个键值对之间用当前参数分隔,第二个参数是指没一个键值对中的键和值之间用当前参数分隔
    dic ={
        'uname':'lili',
        'uage':'30'
    }
    #sort_keys=True 让输出的json串有序
    json_str=json.dumps(dic,sort_keys=True,separators=(':',','))
    s=[
        {
            'uname':'lili',
            'age':18,
        },
        {
            'uname':'panghu',
            'age':20,
        }
    ]
    json_str_arr = json.dumps(s)


    from django.core import serializers
    users=User.objects.all()
    json_str_all=serializers.serialize('json',users)

    # l=[]
    # users=User.objects.all()
    # for i in users:
    #     d={}
    #     d['username']=i.uname
    #     l.append(d)
    #
    # all_json=json.dumps(l)

    return HttpResponse(json_str_arr,content_type='application/json')

    #dajango v2
    # return JsonResponse({'code':10010,'data':{}})

def checkuname(request):
    #1.获取ajax传过来的用户名
    uname=request.GET.get('uname')
    #2 校验用户名是否存在

    users=User.objects.filter(uname=uname).all()
    if users:
        return HttpResponse('1')
    return HttpResponse('0')

def make_post(request):
    if request.method=='GET':
        return render(request,'make_post.html')
    elif request.method=='POST':
        #获取表单数据
        uname=request.POST.get('uname')
        pwd=request.POST.get('pwd')
        return HttpResponse('You post is ok %s %s!!!'%(uname,pwd))
    else:
        raise