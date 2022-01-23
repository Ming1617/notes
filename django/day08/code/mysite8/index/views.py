from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index_view(request):
    print('主页被访问')
    return HttpResponse('主页')

def page1_view(request):
    return HttpResponse('页面1')
