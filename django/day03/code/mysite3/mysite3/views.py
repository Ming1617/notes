
from django.http import HttpResponse
from django.shortcuts import render

def shebao_view(request):
    if request.method=='GET':
        return render(request,'shebao.html')
    elif request.method=='POST':
        base=request.POST.get('base','0')
        base=float(base)
        is_city=request.POST.get('is_city','1')
        yl_gr=base*0.08
        yl_dw=base*0.19
        sy_dw=base*0.008
        if is_city=='1':
            sy_gr=base*0.002
        else:
            sy_gr=0

        return render(request,'shebao.html',locals())

