#file:mysite2/views.py

from django.http import HttpResponse


def sum_view(request):
    #http://127.0.0.1:8000/sum?start=1&stop=101&step=1
    if request.method=='GET':
        try:
            start=request.GET.get('start','0')
            start=int(start)
            stop=request.GET['stop']
            stop=int(stop)
            step=request.GET.get('step','1')
            step=int(step)
            mysum=sum(range(start,stop,step))
            html='和是：%d'%mysum
            return HttpResponse(html)
        except Exception as err:
            return HttpResponse("您给的查询字符串无效！")

login_form_html="""
<form action="/login" method="post">
 用户名:<input name="username" type="text">
 <input type="submit" value="登录">
</form>
"""
def login_view(request):
    if request.method=='GET':
        return HttpResponse(login_form_html)
    elif request.method=='POST':
        name=request.POST.get('username','属性错误')
        html='姓名：'+name
        return HttpResponse(html)

def login2_view(request):
    if request.method=='GET':
        #返回模板生成的html给浏览器
        #方法1
        #1.通过loader加载模板
        # from django.template import loader
        # t=loader.get_template('mylogin.html')
        # #2.用模板生成html
        # html=t.render({"name":"tarena"})
        # #3.将html返回给浏览器
        # return HttpResponse(html)

        #方法2
        from django.shortcuts import render
        return render(request,'mylogin.html',
                {'name':'老魏','passwd':'123456'})

def say_hello():
    return '你好'
class Dog:
    def say(self):
        return '汪汪！'

from django.shortcuts import render
def test_view(request):
    s='Hello Tarena!'
    lst=['北京','上海','重庆']
    mydic={'name':'tedu','age':20}
    dic={'s':s,
         'lst':lst,
         "mydic":mydic,
         "say_hell":say_hello,
         'dog1':Dog()}
    return render(request,'test.html',dic)

def mytemp_view(request):
    # dic={
    #     'x':0
    # }
    x=-4
    return render(request,'mytemp.html',locals())

def mycal_view(request):
    if request.method == 'GET':
        return render(request,'mycal.html')
    if request.method == 'POST':
        x=int(request.POST.get('x', '0'))
        y=int(request.POST.get('y','0'))
        op=request.POST.get('op')
        if op == 'add':
            result=x+y
        elif op=='sub':
            result=x-y
        elif op=='mul':
            result=x*y
        elif op=='div':
            result=x/y
        return render(request,'mycal.html',locals())

def for_view(request):
    lst=['北京','上海','天津']
    s='<i>Hello World!</i>'
    n=100
    s2='aa bb vvv ccc sss'
    return render(request,'for.html',locals())

def index_view(request):
    return render(request,'base.html')

def sport_view(request):
    return render(request,'sport.html')

def news_view(request):
    pass
