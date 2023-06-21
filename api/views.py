import json
import requests
from hashlib import md5
from django.core.mail import send_mail

from django.conf import settings
from django.utils.html import escape
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .Backup import Backuper
from blog.models import Articles
from users.models import Profile


def getQQAvatarLink(qqAccount):
    url1 = f'https://ptlogin2.qq.com/getface?&imgtype=1&uin={qqAccount}'
    reqq = requests.get(url1)
    if reqq.status_code == 200:
        # handle req data
        c = list(reqq.text)
        c.pop()
        c = c[13:] # delete the last 13 characters
        # save url
        c = ''.join(c)
        c = json.loads(c)
        url = c[qqAccount]
        return url

# 同步qq头像：http://q1.qlogo.cn/g?b=qq&nk=666&s=1，nk对应qq号
@login_required
def qqPhoto(request):
    """Sync qq avatar"""
    if request.method == 'POST':
        data = request.POST
        qqAccount = data.get('qqAccount')
        # Data correct, start to handle
        if qqAccount:
            qqAccount = data['qqAccount']
            avatarLink = getQQAvatarLink(qqAccount)
            if avatarLink:
                user = request.user
                user.avatar = avatarLink
                user.save()
                context = {"content": "同步成功"}
                return render(request, 'api/index.html', context)
            else:
                context = {"content": "同步失败"}
                return render(request, 'api/index.html', context)
        # Data is not num
        elif not qqAccount.isdigit():
            context = {"content": "数据不合法"}
            return render(request, 'api/index.html', context)
        # Data is not correct
        else:
            context = {"content": "未检测到数据"}
            return render(request, 'api/index.html', context)
    # Other methods
    context = {"content": "Method not allowed"}
    return render(request, 'api/index.html', context)

@login_required
def gravatarPhoto(request):
    """Sync gravatar"""
    if request.method == 'POST':
        context = dict()
        # Get data
        GravatarAccount = str(request.POST.get('GravatarAccount'))
        # Data correct
        if GravatarAccount:
            md = md5(GravatarAccount.encode()).hexdigest()
            url = f"https://sdn.geekzu.org/avatar/{md}?size=40"
            user = request.user
            user.avatar = url
            user.save()
            context['content'] = '同步成功'
            return render(request, 'api/index.html', context)
        else:
            context['content'] = '未检测到数据'
            return render(request, 'api/index.html', context)
    # Other methods
    context = {"content": "Method not allowed"}
    return render(request, 'api/index.html', context)

@login_required
def sendEmail(request):
    """Send Email"""
    if request.method == 'POST':
        message = request.POST.get('message')
        # POST data check
        if isinstance(message, str):
            message = escape(message)
            # Length check
            if len(message) <= 1000 and message.strip() != '':
                targetUser = request.user
                
                subject = 'Share And Talk用户反馈' # Email subject
                message += f'\n\n来自用户:\nID:{targetUser.id}\n昵称:{targetUser.nickname}'
                send_mail(subject, message, None, settings.DEFAULT_RECIPIENT_LIST)
                
                # Set cookie
                req = redirect('blog:index')
                sign = 'sendEmailSuccess'
                req.set_signed_cookie('sign', sign, max_age=60, salt=settings.SECRET_KEY)
                
                return req

    req = redirect('blog:index')
    sign = 'sendEmailFailed'
    req.set_signed_cookie('sign', sign, max_age=60, salt=settings.SECRET_KEY)
    return req

@login_required
def like(request):
    """Handle article like"""
    if request.method == 'POST':
        # Handle post
        data = request.POST.get('article_id', False)
        # No data
        if not data:
            return HttpResponse('failed')
        data = str(data)
        # Data is not num
        if not data.isdigit():
            return HttpResponse('failed')
        article = get_object_or_404(Articles, id=data)
        # If already liked
        if request.user in article.likes.all():
            article.likes.remove(request.user)
            return HttpResponse('dislike ok')
        article.likes.add(request.user)
        return HttpResponse('like ok')
    return HttpResponse('failed')

@login_required
def backupDB(request):
    content = 'failed'
    if request.method == 'GET':
        # Check superuser
        if request.user.is_superuser:
            # Backup database
            bbackup = Backuper()
            content = bbackup.backup()
    context = {'content': content}
    return render(request, 'api/index.html', context)
