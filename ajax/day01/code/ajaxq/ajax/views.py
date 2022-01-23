import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def load_test(request):
    return render(request,'load_test.html')

def load_test_server(request):
    return render(request,'load_test_server.html')

def jquery_get(request):
    return render(request,'jquery_get.html')

def jquery_get_server(request):
    uname=request.GET.get('uname','meinadao')
    age=request.GET.get('age','age meinadao')
    d={
        'uname':uname,
        'age':age
    }
    #指定httpresponse响应头
    return HttpResponse(json.dumps(d),content_type='application/json')

def jquery_post(request):
    return render(request,'jquery_post.html')

def jquery_post_server(request):
    if int(request.GET.get('age',0))>100:
        d = {'msg': 'Your age is so big!', 'code': 1202}
        return HttpResponse(json.dumps(d), content_type='application/json')
    d={'msg':'post is ok','code':1201}
    return HttpResponse(json.dumps(d),content_type='application/json')

def jquery_ajax(reqyest):
    return render(reqyest,'jquery_ajax.html')

def jquery_ajax_server(request):
    import time
    time.sleep(3)
    obj={'name':'guoxiaonao','age':18}
    return HttpResponse(json.dumps(obj),content_type='application/json')

def jquery_ajax_user(request):
    return render(request,'jquery_ajax_user.html')

def jquery_ajax_user_server(request):
    d=[{'name':'guoxiaonao','age':18},
       {'name':'laowang','age':39}]
    return HttpResponse(json.dumps(d),content_type='application/json')

def cross(request):
    return render(request,'cross.html')

def cross_server(request):
    func=request.GET.get('callback')
    #func('str')
    return HttpResponse(func+"('w kua chu lai le hahah1')")

def cross_server_json(request):
    func=request.GET.get('callback')
    d={'name':'admin','age':10}
    return HttpResponse(func+"("+json.dumps(d)+")")