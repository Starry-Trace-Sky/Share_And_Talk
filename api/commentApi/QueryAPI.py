"""
=================================================
@Project -> File    ：Share_And_Talk -> queryAPI
@IDE                ：PyCharm
@Author             ：Skyler Sun
@Date               ：2023/6/22 16:55
@用途               ：处理查询评论逻辑
@email              ：65846869+Skyler-Sun@users.noreply.github.com
==================================================
"""
from django.views import View
from django.http import JsonResponse, HttpResponseNotAllowed
from django.shortcuts import HttpResponse, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from blog.models import Articles


@method_decorator(login_required, name='get')
class QueryComment(View):
    def __init__(self):
        super().__init__()
        self.text = None
        self.articleID = None
        self.article = None
        self.responseData = dict(data=list())

    def get(self, request):
        """处理get请求"""
        self.__getData(request)
        if not self.__checkData():
            return HttpResponse(self.text)
        self.__queryData()
        return JsonResponse(self.responseData)

    def __queryData(self):
        """查询数据"""
        comments = self.article.comments_set.order_by('-pubDate')
        for comment in comments:
            tempData = {
                'avatarLink': comment.author.avatar,
                'nickName': comment.author.nickName,
                'text': comment.content,
                'likesCount': comment.likes.count()
            }
            self.responseData['data'].append(tempData)

    def __getData(self, req):
        """获取文章id"""
        self.articleID = req.GET.get('articleID')

    def __checkData(self):
        """验证id有效性"""
        self.articleID = str(self.articleID)
        if not self.articleID.isdigit():
            self.text = '文章id无效'
        else:
            self.articleID = int(self.articleID)
            self.article = get_object_or_404(Articles, pk=self.articleID,
                                             public=True)
            return True

    def http_method_not_allowed(self, request, *args, **kwargs):
        """其他请求"""
        self.text = "方法不允许"
        return HttpResponseNotAllowed(['GET'], self.text)
