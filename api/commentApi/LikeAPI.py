"""
=================================================
@Project -> File    ：Share_And_Talk -> LikeAPI
@IDE                ：PyCharm
@Author             ：Skyler Sun
@Date               ：2023/6/22 17:16
@用途               ：处理点赞评论
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
class LikeComment(View):
    def __init__(self):
        super().__init__()
        self.data = None
        self.commentID = None
        self.comment = None
        self.text = None

    def post(self, request):
        """处理post请求"""
        self.data = request.POST
        if self.__checkData():
            self.__handleLike(request)
            return HttpResponse(self.text)
        
    def __checkData(self):
        """校验数据"""
        self.commentID = str(self.data.get('commentID'))
        # 校验不为空，为数字
        if self.commentID and self.commentID.isdigit():
            self.comment = get_object_or_404(Comments, pk=self.commentID)
            return True
        
    def __handleLike(self, req):
        """处理点赞"""
        # 已点赞，取消点赞
        if self.comment.likes.contains(req.user):
            self.comment.likes.remove(req.user)
            self.text = "取消点赞成功"
        # 未点赞，点赞
        else:
            self.comment.likes.add(req.user)
            self.text = "点赞成功"

    def http_method_not_allowed(self, request, *args, **kwargs):
        """其他请求""" 
        return HttpResponseNotAllowed("方法不允许")
