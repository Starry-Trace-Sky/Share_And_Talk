from django.db.models import Q
from django.http import Http404
from django.shortcuts import render

from .models import Articles, TopMetas, SecondMetas
from soft.models import SoftMetas


def search(request):
    """搜索"""
    request.encoding = 'utf-8'
    if request.method == 'GET':
        key = request.GET.get('s')
        if key:
            # 查询文章
            # 未登录，隐藏私密文章
            if not request.user.is_authenticated:
                articles = Articles.objects.order_by('-pub_date').filter(
                    public=True)
            # 已登录，隐藏除自己外的私密文章
            else:
                articles = (Articles.objects.order_by('-pub_date').filter(
                    Q(public=True) | Q(public=False, author=request.user)))
            result = []
            for i in articles:
                if key in i.title:
                    result.append(i)

            topMetas = TopMetas.objects.all().order_by('id')
            secondMetas = SecondMetas.objects.all().order_by('id')
            softMetas = SoftMetas.objects.all().order_by('id')
            # 未查出
            if len(result) == 0:
                context = {
                    'topMetas': topMetas,
                    'secondMetas': secondMetas,
                    'softMetas': softMetas,
                }
                return render(request, 'blog/index.html', context)
            # 查出
            else:
                # 返回页面
                context = {
                    'title': 'Share And Talk-搜索结果',
                    'topMetas': topMetas,
                    'secondMetas': secondMetas,
                    'softMetas': softMetas,
                    'articles': result,
                    'keyWords': key
                }
                return render(request, 'blog/search.html', context)
    # 其他情况
    raise Http404
