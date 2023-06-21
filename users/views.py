import re
import uuid

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.conf import settings

from users.models import Profile


class CustomLoginView(LoginView):
    template_name = 'registration/login.html' # 自定义登录页面的模板
    success_url = reverse_lazy('blog:index') # 用户成功登录后重定向的URL

    def form_valid(self, form):
        # 在这里处理表单验证成功后的逻辑
        # 添加自定义cookie
        response = super().form_valid(form)
        response.set_signed_cookie('sign', 'loginSuccess',
                                   salt=settings.SECRET_KEY)
        return response


def validate_name(name):
    """检验name是否只包含数字，字母@ . - _"""
    pattern = r'^[a-zA-Z0-9@.\-_]+$'
    return bool(re.match(pattern, name))

def register(request):
    """注册页面"""
    sign = None
    if request.method != 'POST':
        # 显示空表单
        form = RegisterForm()
    else:
        form = RegisterForm(data=request.POST)

        if form.is_valid():
            new_user = form.save(commit=False)
            if validate_name(new_user.username):
                new_user.save()
                # 让用户自动登录，重新向至主页
                login(request, new_user)
                req = redirect('blog:index')
                sign = 'registerSuccess'
                req.set_signed_cookie('sign', sign, max_age=60, salt=settings.SECRET_KEY)
                return req
            
            else:
                sign = '用户名格式错误'
    
    # 显示空表单或指出表单无效
    context = {
        'form': form,
        'sign': sign
    }
    return render(request, 'registration/register.html', context)
