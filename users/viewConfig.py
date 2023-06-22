from django.shortcuts import HttpResponse, render

# TODO:实现用户中心功能
def index(request):
    """用户中心首页"""
    return render(request, 'users/index.html')
