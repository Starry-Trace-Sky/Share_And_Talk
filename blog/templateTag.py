"""
自定义模板函数
"""
from django.template.defaulttags import register


@register.filter
def get_range(value):
    """实现模板range函数"""
    return range(1, value+1)
