from django.http import Http404
from django.shortcuts import get_object_or_404

from .common import getSign
from .models import TopMetas, SecondMetas, Articles
from soft.models import SoftMetas


def Help(request):
    """帮助页面"""
    user = False
    loginStatus = False
    like = False
    passage = get_object_or_404(Articles, title="使用帮助")
    if request.user == passage.author:
        user = True
    if request.user.is_authenticated:
        loginStatus = True
    if request.user in passage.likes.all():
        like = True
    passage.read_times += 1
    passage.save()
    topMetas = TopMetas.objects.all().order_by('id')
    secondMetas = SecondMetas.objects.all().order_by('id')
    softMetas = SoftMetas.objects.all().order_by('id')
    context = {
        'title': f"Share And Talk-{passage.title}",
        'topMetas': topMetas,
        'secondMetas': secondMetas,
        'text': passage.getHTML(),
        'softMetas': softMetas,
        'users': user,
        'passage': passage,
        'login': loginStatus,
        'like': like
    }
    req = getSign(request, 'blog/article/articles.html', context)
    return req


def article(request, year, month, day, id):
    """文章页面"""
    user = False
    loginStatus = False
    like = False
    passage = get_object_or_404(Articles, id=id)
    if (passage.pub_date.year != year) or (passage.pub_date.month != month) or (
            passage.pub_date.day != day):
        raise Http404
    if (request.user != passage.author) and not passage.public:
        raise Http404
    if request.user == passage.author:
        user = True
    if request.user.is_authenticated:
        loginStatus = True
    if request.user in passage.likes.all():
        like = True
    passage.read_times += 1
    passage.save()
    topMetas = TopMetas.objects.all().order_by('id')
    secondMetas = SecondMetas.objects.all().order_by('id')
    softMetas = SoftMetas.objects.all().order_by('id')
    context = {
        'title': f"Share And Talk-{passage.title}",
        'topMetas': topMetas,
        'secondMetas': secondMetas,
        'text': passage.getHTML(),
        'softMetas': softMetas,
        'users': user,
        'passage': passage,
        'login': loginStatus,
        'like': like
    }
    req = getSign(request, 'blog/article/articles.html', context)
    return req
