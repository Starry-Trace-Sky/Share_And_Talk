"""
=================================================
@Project -> File    ：Share_And_Talk -> qqAvatar.py
@IDE                ：PyCharm
@Author             ：Skyler Sun
@Date               ：2023/6/22 15:43
@用途               ：
@email              ：65846869+Skyler-Sun@users.noreply.github.com
==================================================
"""
import requests
import json

from django.views import View
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required, name='post')
class QQAvatar(View):
    # 同步qq头像：http://q1.qlogo.cn/g?b=qq&nk=666&s=1，nk对应qq号
    def __init__(self):
        super().__init__()
        self.qqAccount = None
        self.context = None
        self.avatarUrl = None
        self.context = dict(context='')

    def __getQQAvatarLink(self):
        """获取qq头像链接"""
        url1 = f'https://ptlogin2.qq.com/getface?&imgtype=1&uin={self.qqAccount}'
        reqq = requests.get(url1)
        if reqq.status_code == 200:
            # handle req data
            c = list(reqq.text)
            c.pop()
            c = c[13:]  # delete the last 13 characters
            # save url
            c = ''.join(c)
            c = json.loads(c)
            url = c[self.qqAccount]
            self.avatarUrl = url
            return True

    def __getData(self, req):
        """初始化数据"""
        self.qqAccount = req.POST.get('qqAccount')
        if self.qqAccount:
            return True

    def __checkData(self):
        """验证数据"""
        self.qqAccount = str(self.qqAccount)
        # qq账号不全为数字
        # qq账号符合规范
        if self.qqAccount:
            return True

    def post(self, request):
        """处理post请求"""
        # 无数据
        req = request
        if not self.__getData(req):
            self.context['content'] = "未检测到数据"
            return render(request, 'api/index.html', self.context)
        # 数据不全是数字
        if not self.__checkData():
            self.context['content'] = "qq账号不全为数字"
            return render(request, 'api/index.html', self.context)
        # 获取连接出错
        if not self.__getQQAvatarLink():
            self.context['content'] = '获取链接出错'
            return render(request, 'api/index.html', self.context)
        user = request.user
        user.avatar = self.avatarUrl
        user.save()
        self.context['content'] = "同步成功"
        return render(request, 'api/index.html', self.context)

    def http_method_not_allowed(self, request, *args, **kwargs):
        """其他请求"""
        self.context['content'] = "方法不允许"
        return render(request, 'api/index.html', self.context)
