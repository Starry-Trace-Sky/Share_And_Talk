from django.http import Http404
from django.utils import timezone
from django.conf import settings
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .form import ArticleForm
from .models import Articles, TopMetas, SecondMetas
from soft.models import SoftMetas


@login_required
def newArticle(request):
    """新建文章"""
    if request.method != 'POST':
        # 未提交数据，创建新表单
        form = ArticleForm()
    else:
        # POST提交的数据，对数据处理
        form = ArticleForm(data=request.POST)
        pbc = request.POST.get('pb', False)
        if pbc == 'on':
            pbc = True
        if not isinstance(pbc, bool):
            return redirect('blog:new_article')
        if form.is_valid():
            new_article = form.save(commit=False)
            new_article.author = request.user
            new_article.public = pbc
            new_article.pub_date = timezone.now()
            new_article.save()
            datte = new_article.pub_date
            # 设置提示框需要的cookie
            req = redirect('blog:article', year=datte.year, month=datte.month,
                           day=datte.day, id=new_article.id)
            sign = 'createSuccess'
            req.set_signed_cookie('sign', sign, max_age=60,
                                  salt=settings.SECRET_KEY)
            return req
    topMetas = TopMetas.objects.all().order_by('id')
    secondMetas = SecondMetas.objects.all().order_by('id')
    softMetas = SoftMetas.objects.all().order_by('id')
    form = ArticleForm()
    context = {
        'title': 'Share And Talk-新建文章',
        'topMetas': topMetas,
        'secondMetas': secondMetas,
        'softMetas': softMetas
    }
    # 返回编辑页面
    return render(request, 'blog/markdown/newArticle.html', context)


@login_required
def editArticle(request, id):
    """编辑文章"""
    targetArticle = get_object_or_404(Articles, pk=id)
    if targetArticle.author != request.user:
        raise Http404
    if request.method != 'POST':
        # 未提交数据，创建新表单
        form = ArticleForm(instance=targetArticle)
    elif request.method == 'POST':
        # POST提交的数据，对数据处理
        pbc = request.POST.get('pb', False)
        if pbc == 'on':
            pbc = True
        if not isinstance(pbc, bool):
            return redirect('blog:edit_article', id=id)
        form = ArticleForm(instance=targetArticle, data=request.POST)
        if form.is_valid():
            # 重定向至首页
            new_article = form.save(commit=False)
            new_article.id = id
            new_article.modify_date = timezone.now()
            new_article.public = pbc
            datte = new_article.pub_date
            # 设置sign
            req = redirect('blog:article', year=datte.year, month=datte.month,
                           day=datte.day, id=new_article.id)
            sign = 'editSuccess'
            req.set_signed_cookie('sign', sign, max_age=60,
                                  salt=settings.SECRET_KEY)
            new_article.save()
            return req
    topMetas = TopMetas.objects.all().order_by('id')
    secondMetas = SecondMetas.objects.all().order_by('id')
    softMetas = SoftMetas.objects.all().order_by('id')
    form = ArticleForm()
    context = {
        'title': 'Share And Talk-编辑文章',
        'topMetas': topMetas,
        'secondMetas': secondMetas,
        'article': targetArticle,
        'softMetas': softMetas
    }
    # 返回编辑页面
    return render(request, 'blog/markdown/editArticle.html', context)


@login_required
def deleteArticle(request, id):
    """删除文章"""
    passage = get_object_or_404(Articles, pk=id)
    if request.user == passage.author:
        passage.delete()
        # 设置sign
        req = redirect('blog:index')
        sign = 'deleteSuccess'
        req.set_signed_cookie('sign', sign, max_age=60,
                              salt=settings.SECRET_KEY)
        return req
    else:
        raise Http404
