from django.conf import settings

from django.utils.html import escape
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .Backup import Backuper
from blog.models import Articles


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

                subject = 'Share And Talk用户反馈'  # Email subject
                message += f'\n\n来自用户:\nID:{targetUser.id}\n昵称:{targetUser.nickName}'
                send_mail(subject, message, None,
                          settings.DEFAULT_RECIPIENT_LIST)

                # Set cookie
                req = redirect('blog:index')
                sign = 'sendEmailSuccess'
                req.set_signed_cookie('sign', sign, max_age=60,
                                      salt=settings.SECRET_KEY)

                return req

    req = redirect('blog:index')
    sign = 'sendEmailFailed'
    req.set_signed_cookie('sign', sign, max_age=60,
                          salt=settings.SECRET_KEY)
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
