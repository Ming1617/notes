from django.http import HttpResponse,JsonResponse


def test_cros(request):
    return HttpResponse("测试网页")