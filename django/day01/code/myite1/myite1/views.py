#fiel:mysite1/views.py

from django.http import HttpResponse
from django.http import HttpResponseRedirect

index_html='''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<a href="/mypage?a=888&b=999">进入mypage</a>
<form action="/mypage" method="get">
    <input type="text" name="a">
    <input type="text" name="b">
    <input type="submit" value="提交">
</form>
</body>
</html>
'''

def page1_view(request):
    html='<h1>这是第1个页面</h1>'
    return HttpResponse(html)

def index_view(request):
    # html='<h1>这是主页面</h1>'
    return HttpResponse(index_html)

def page2_view(request):
    html='<h1>这是第2个页面</h1>'
    return HttpResponse(html)

def pagen_view(request,n=None):
    html = '<h1>=====这是第%s个页面</h1>'%n
    return HttpResponse(html)

def math_view(request,x,op,y):
    x=int(x) #转为整数
    y=int(y)
    result=None
    if op=='add':
        result=x+y
    elif op=='sub':
        result=x-y
    elif op=='mul':
        result=x*y
    if result is None:
        # return HttpResponse('出错了！')
        return HttpResponseRedirect('https://www.baidu.com')
    html='结果是：'+str(result)
    html+='您的ip地址是：'+request.META['REMOTE_ADDR']
    print(html)
    return HttpResponse(html)

def person_view(request,name=None,age=None):
    s='姓名：'+name
    s+='年龄:'+age
    return HttpResponse(s)
    # s=str(kwargs)
    # return HttpResponse(s)

def birthday_view(request,y,m,d):
    print(y,m,d)
    html='生日：%s年%s月%s日'%(y,m,d)
    return HttpResponse(html)

def mypage_view(request):
    '''
        此视图函数用来表示得到的GET请求中的查询参数
        http://127.0.0.1:8000/mypage?a=100&b=200
    :param request:
    :return:
    '''
    if request.method =='GET':
        # a=request.GET['a']
        a = request.GET.get('a','没有对应的值')
        # b=request.GET['b']
        b = request.GET.getlist('b')

        html='a='+a
        html+='b='+str(b)
        return HttpResponse(html)
    else:
        return HttpResponse('当前不是get请求')