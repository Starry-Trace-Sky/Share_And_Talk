from django.shortcuts import redirect, render, HttpResponse

from soft.models import SoftMetas
from blog.models import TopMetas, SecondMetas, Articles


def queryComment(request):
    """查询评论"""
    if request.method == 'GET':
        pass
    return HttpResponse('ok')


def addComment(request):
    """添加评论"""
    if request.method == 'POST':
        pass
    return redirect('blog:index')


def editComment(request):
    """编辑评论"""
    if request.method == 'POST':
        pass
    return redirect('blog:index')


def deleteComment(request):
    """删除评论"""
    if request.method == 'POST':
        pass
    return redirect('blog:index')
