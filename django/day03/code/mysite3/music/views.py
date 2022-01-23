from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def page1_view(request):
    return HttpResponse('页面1')

def page2_view(request):
    return HttpResponse('页面2')

def page3_view(request):
    return HttpResponse('页面3')

def index_view(request):
    return HttpResponse('音乐首页')