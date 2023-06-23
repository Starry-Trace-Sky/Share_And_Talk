"""
=================================================
@Project -> File    ：Share_And_Talk -> forms
@IDE                ：PyCharm
@Author             ：Skyler Sun
@Date               ：2023/6/22 20:48
@用途               ：
@email              ：65846869+Skyler-Sun@users.noreply.github.com
==================================================
"""
from django import forms
from comment.models import Comments


class CommentForm(forms.ModelForm):
    """
    基于Comments的表单
    需要填写的字段：
    article：文章id(后台要更换为对象)
    parent: 父级标签id(后台要更换为对象)
    content: 评论内容
    需要代码指定的字段:
    author: 作者(request.user)

    """

    class Meta:
        model = Comments
        fields = ['article', 'parent', 'content']
        labels = {}
