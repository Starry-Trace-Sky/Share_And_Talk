from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage  # 页数

from .models import TopMetas, SecondMetas, Articles
from soft.models import SoftMetas


def metas_top(request, id, pageID):
    """一级分类页面"""
    targetMeta = get_object_or_404(TopMetas, pk=id)
    topMetas = TopMetas.objects.all().order_by('id')
    secondMetas = SecondMetas.objects.all().order_by('id')
    softMetas = SoftMetas.objects.all().order_by('id')
    # 未登录，隐藏私密文章
    if not request.user.is_authenticated:
        articles = Articles.objects.order_by('-pub_date').filter(meta_top=id,
                                                                 public=True)
    # 已登录，隐藏除自己外的私密文章
    else:
        articles = (Articles.objects.order_by('-pub_date').filter(
            Q(meta_top=id, public=True) | Q(meta_top=id, public=False,
                                            author=request.user)))
    paginator = Paginator(articles, 6)  # 将文章列表分页，每页显示 6 篇博客文章
    pageNumber = request.GET.get('page')  # 获取当前页码，默认为第一页

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
    """
    页数
    pageCount = articles.count()
    pageCountR = pageCount % 6
    pageCount //= 6
    if pageCountR != 0:
        pageCount += 1
    if pageCount == 0:
        pass
    elif pageID > pageCount:
        raise Http404
    # 切片文章
    a = (pageID-1)*6
    b = a + 6
    articles = articles[a:b]
    """
    context = {
        'title': f'Share And Talk-一级分类-{targetMeta.text}',
        'topMetas': topMetas,
        'secondMetas': secondMetas,
        'articles': articles,
        'softMetas': softMetas,
        # 'pageCount': pageCount,
        'currentPage': pageID,
        'currentMetaID': targetMeta.id
    }
    return render(request, 'blog/index.html', context)


def metas_second(request, id, pageID):
    """二级分类页面"""
    targetMeta = get_object_or_404(SecondMetas, pk=id)
    topMetas = TopMetas.objects.all().order_by('id')
    secondMetas = SecondMetas.objects.all().order_by('id')
    softMetas = SoftMetas.objects.all().order_by('id')
    # 未登录，隐藏私密文章
    if not request.user.is_authenticated:
        articles = Articles.objects.order_by('-pub_date').filter(meta_second=id,
                                                                 public=True)
    # 已登录，隐藏除自己外的私密文章
    else:
        articles = (Articles.objects.order_by('-pub_date').filter(
            Q(meta_second=id, public=True) | Q(meta_second=id, public=False,
                                               author=request.user)))

    paginator = Paginator(articles, 6)  # 将文章列表分页，每页显示 6 篇博客文章
    pageNumber = request.GET.get('page')  # 获取当前页码，默认为第一页

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
    """
    页数
    pageCount = articles.count()
    pageCountR = pageCount % 6
    pageCount //= 6
    if pageCountR != 0:
        pageCount += 1
    if pageCount == 0:
        pass
    elif pageID > pageCount:
        raise Http404
    # 切片文章
    a = (pageID-1)*6
    b = a + 6
    articles = articles[a:b]
    """
    context = {
        'title': f'Share And Talk-二级分类-{targetMeta.text}',
        'topMetas': topMetas,
        'secondMetas': secondMetas,
        'articles': articles,
        'softMetas': softMetas,
        # 'pageCount': pageCount,
        'currentPage': pageID,
        'currentMetaID': targetMeta.id
    }
    return render(request, 'blog/index.html', context)


def metas_software(request, id, pageID):
    """软件分类页面"""
    targetMeta = get_object_or_404(SoftMetas, pk=id)
    topMetas = TopMetas.objects.all().order_by('id')
    secondMetas = SecondMetas.objects.all().order_by('id')
    softMetas = SoftMetas.objects.all().order_by('id')
    targetSoft = get_object_or_404(SoftMetas, pk=id)
    articles = Articles.objects.order_by('-pub_date')
    # 页数
    pageCount = articles.count()
    pageCountR = pageCount % 6
    pageCount //= 6
    if pageCountR != 0:
        pageCount += 1
    if pageCount == 0:
        pass
    elif pageID > pageCount:
        raise Http404
    # 切片文章
    a = (pageID - 1) * 6
    b = a + 6
    articles = articles[a:b]
    context = {
        'title': f'Share And Talk-软件分类-{targetMeta.text}',
        'topMetas': topMetas,
        'secondMetas': secondMetas,
        'articles': articles,
        'softMetas': softMetas,
        'softCurrent': targetSoft,
        'pageCount': pageCount,
        'currentPage': pageID
    }
    return render(request, 'blog/software.html', context)


@login_required
def myArticles(request):
    """我的文章"""
    page = request.GET.get('page', 1)
    topMetas = TopMetas.objects.all().order_by('id')
    secondMetas = SecondMetas.objects.all().order_by('id')
    softMetas = SoftMetas.objects.all().order_by('id')
    articles = Articles.objects.order_by('-pub_date').filter(
        author=request.user)
    paginator = Paginator(articles, 6)

    try:
        articles = paginator.page(page)
    except:
        return redirect('blog:my_articles')

    context = {
        'title': 'Share And Talk-我的文章',
        'topMetas': topMetas,
        'secondMetas': secondMetas,
        'articles': articles,
        'softMetas': softMetas
    }
    return render(request, 'blog/index.html', context)
