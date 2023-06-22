"""
=================================================
@Project -> File    ：Share_And_Talk -> DelAPI.py
@IDE                ：PyCharm
@Author             ：Skyler Sun
@Date               ：2023/6/22 16:56
@用途               ：处理删除评论
@email              ：3385213313@qq.com
==================================================
"""
from django.views import View
from django.http import HttpResponseNotAllowed
from django.shortcuts import HttpResponse, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from comment.models import Comments


@method_decorator(login_required, name='post')
class DelComment(View):
    def __init__(self):
        super().__init__()
        # 变量初始化
        self.data = None
        self.commentID = None
        self.comment = None

    def post(self, request):
        """处理post请求"""
        self.data = request.POST
        if self.__checkData():
            if request.user == self.comment.author:
                self.comment.delete()
                return HttpResponse('ok')
            return HttpResponse('你不是评论发布者')
        return HttpResponse('failed')
        
    def __checkData(self):
        """校验数据"""
        self.commentID = str(self.data.get('commentID'))
        # 验证评论id不为空，只为数字
        if self.commentID and self.commentID.isdigit():
            self.commentID = int(self.commentID)
            # 获取评论
            self.comment = get_object_or_404(Comments, pk=self.commentID)
            return True

    def http_method_not_allowed(self, request, *args, **kwargs):
        """其他请求"""
        return HttpResponseNotAllowed("方法不允许")
