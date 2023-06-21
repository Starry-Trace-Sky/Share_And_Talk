from django.db.models import Q
from django.shortcuts import redirect, render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage # 页数

from .common import getSign
from .models import TopMetas, SecondMetas, Articles
from soft.models import SoftMetas


def index(request):
    """首页"""
    return redirect('blog:pages')

def pages(request):
    """页数"""
    topMetas = TopMetas.objects.all().order_by('id')
    secondMetas = SecondMetas.objects.all().order_by('id')
    softMetas = SoftMetas.objects.all().order_by('id')
    # 未登录，隐藏私密文章
    if not request.user.is_authenticated:
        articles = Articles.objects.order_by('-pub_date').filter(public=True)
    # 已登录，隐藏除自己外的私密文章
    else:
        articles = (Articles.objects.order_by('-pub_date').filter(
                        Q(public=True) | Q(public=False, author=request.user)))
    
    paginator = Paginator(articles, 6) # 将文章列表分页，每页显示 6 篇博客文章
    pageNumber = request.GET.get('page') # 获取当前页码，默认为第一页
    
    try:
        articles = paginator.page(pageNumber)
    except PageNotAnInteger:
        # 如果 page 参数不是一个整数，就显示第一页
        articles = paginator.page(1)
        pageNumber = 1
    except EmptyPage:
        # 如果请求的页码超出了最大页数，则显示最后一页
        articles = paginator.page(paginator.num_pages)
        pageNumber = paginator.num_pages

    # 如果 URL 中的 page 参数不正确，则重定向到正确的 URL
    if int(pageNumber) != articles.number:
        return redirect('pages', page=articles.number)
    context = {
        'title' : f'Share And Talk-第{pageNumber}页',
        'topMetas': topMetas,
        'secondMetas': secondMetas,
        'articles': articles,
        'softMetas': softMetas,
        #'pageCount': pageCount,
        'currentPage': id,
    }
    req = getSign(request, 'blog/index.html', context)
    return req
