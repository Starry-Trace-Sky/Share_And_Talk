"""
=================================================
@Project -> File    ：Share_And_Talk -> addAPI
@IDE                ：PyCharm
@Author             ：Skyler Sun
@Date               ：2023/6/22 16:55
@用途               ：处理增添评论逻辑
@email              ：65846869+Skyler-Sun@users.noreply.github.com
==================================================
"""
from django.views import View
from django.http import Http404, HttpResponseNotAllowed
from django.shortcuts import HttpResponse, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from blog.models import Articles
from api.forms import CommentForm


@method_decorator(login_required, name='post')
class AddComment(View):
    def __init__(self):
        super().__init__()
        self.data = None
        self.newForm = None
        self.article = None

    def post(self, request):
        """处理post请求"""
        self.data = request.POST
        self.newForm = CommentForm(data=self.data)
        # 数据符合规定，补充数据
        if self.newForm.is_valid():
            self.newForm = self.newForm.save(commit=False)
            self.newForm.author = request.user
            self.newForm.save()
            return HttpResponse('ok')
        return HttpResponse('failed')

    def http_method_not_allowed(self, request, *args, **kwargs):
        """其他请求"""
        return HttpResponseNotAllowed(['POST'], '方法不允许')
