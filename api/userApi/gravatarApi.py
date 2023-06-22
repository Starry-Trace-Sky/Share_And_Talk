"""
=================================================
@Project -> File    ：Share_And_Talk -> gravatarApi
@IDE                ：PyCharm
@Author             ：Skyler Sun
@Date               ：2023/6/22 16:36
@用途               ：
@email              ：3385213313@qq.com
==================================================
"""
from hashlib import md5

from django.views import View
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required, name='post')
class GravatarSync(View):
    def __init__(self):
        super().__init__()
        self.context = dict(content='')
        self.GravatarAccount = None
        self.gravatarUrl = None

    def post(self, request):
        # 无数据
        if not self.__checkData(request):
            self.context['content'] = '未检测到数据'
            return render(request, 'api/index.html', self.context)
        # 有数据
        else:
            self.__getUrl()
            self.__save(request)
            self.context['content'] = '同步成功'
            return render(request, 'api/index.html', self.context)

    def __save(self, req):
        """保存数据"""
        user = req.user
        user.avatar = self.gravatarUrl
        user.save()

    def __getUrl(self):
        """获取gravatar链接"""
        md = md5(self.GravatarAccount.encode()).hexdigest()
        url = f"https://sdn.geekzu.org/avatar/{md}?size=40"
        self.gravatarUrl = url

    def __checkData(self, req):
        """验证和初始化数据"""
        self.GravatarAccount = str(req.POST.get('GravatarAccount'))
        if self.GravatarAccount:
            return True

    def http_method_not_allowed(self, request, *args, **kwargs):
        """其他请求"""
        self.context['content'] = "方法不允许"
        return render(request, 'api/index.html', self.context)
