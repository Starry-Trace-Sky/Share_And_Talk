"""
=================================================
@Project -> File    ：Share_And_Talk -> EditAPI.py
@IDE                ：PyCharm
@Author             ：Skyler Sun
@Date               ：2023/6/22 16:56
@用途               ：处理修改评论
@email              ：65846869+Skyler-Sun@users.noreply.github.com
==================================================
"""
from django.views import View
from django.http import HttpResponseNotAllowed
from django.shortcuts import HttpResponse, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from comment.models import Comments
from api.forms import CommentForm


@method_decorator(login_required, name='post')
class ModifyComment(View):
    def __init__(self):
        super().__init__()
        self.data = None
        self.newForm = None
        self.comment = None

    def post(self, request):
        """处理post请求"""
        self.data = request.POST
        self.comment = self.data.get('commentID', False)
        # 数据完备，修改储存数据
        self.newForm = CommentForm(data=self.data)
        if self.newForm.is_valid():
            try:
                # 获取已有评论
                self.comment = get_object_or_404(Comments, pk=self.comment)
            except:
                return HttpResponse('failed')
            # 评论发布者和请求者同一个人
            if request.user == self.comment.author:
                tempForm = self.newForm.save(commit=False)
                # 同一篇文章，内容更改
                if (tempForm.content != self.comment.content) and (tempForm.article == self.comment.article):
                    self.__modifyData()
                    return HttpResponse('ok')
        return HttpResponse('failed')
    
    def __modifyData(self):
        """修改数据"""
        self.comment.content = self.newForm.cleaned_data['content']
        self.comment.save()

    def http_method_not_allowed(self, request, *args, **kwargs):
        """其他请求"""
        return HttpResponseNotAllowed(['POST'], "方法不允许")
