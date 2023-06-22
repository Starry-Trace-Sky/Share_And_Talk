from django.db import models
from django.conf import settings

from blog.models import Articles
from users.models import Profile


class Comments(models.Model):
    """评论"""
    article = models.ForeignKey(Articles, on_delete=models.CASCADE,
                                verbose_name="所属文章", blank=False,
                                null=False)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE,
                               verbose_name="发布者", blank=False, null=False)
    # 父级评论
    parent = models.ForeignKey('self', on_delete=models.CASCADE,
                               verbose_name="父级评论", help_text="可以为空",
                               blank=True, null=True)
    content = models.CharField(max_length=200, verbose_name="评论内容",
                               blank=False, null=False)
    pubDate = models.DateTimeField(auto_now_add=True, verbose_name="发布日期",
                                   editable=False)
    modifyDate = models.DateTimeField(auto_now=True,
                                      verbose_name="修改日期",
                                      editable=False)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                   related_name='likers', verbose_name="点赞",
                                   blank=True)

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = verbose_name

    def __str__(self) -> str:
        description = '[' + self.article.title + ']['
        description += self.author.nickName + ']' + self.content[:20]
        return description
