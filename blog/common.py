from django.conf import settings
from django.shortcuts import render
import pysnooper


def getSign(rq, template, context):
    """
    获取sign标志后的request
    : rq request
    : template 模板路径
    : context 参数
    : return (sign, req)
    """
    try:
        ssign = rq.get_signed_cookie('sign', salt=settings.SECRET_KEY)
    except KeyError:
        ssign = None
    Context = context
    Context['sign'] = ssign
    req = render(rq, template, Context)
    req.delete_cookie('sign')
    return req
