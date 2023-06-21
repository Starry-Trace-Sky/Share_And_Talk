import re
import markdown
from django.db import models
from django.utils.html import strip_tags
from django.conf import settings
from django.utils import timezone

import fontawesome
from emoji import emojize
from mdeditor.fields import MDTextField


class TopMetas(models.Model):
    """一级分类"""
    text = models.CharField(max_length=20, verbose_name="分类名称", 
                            unique=True)
    
    
    class Meta:
        verbose_name = "一级分类"
        verbose_name_plural = "一级分类"
        
    def __str__(self):
        return self.text
    

class SecondMetas(models.Model):
    """二级分类"""
    text = models.CharField(max_length=20, verbose_name="分类名称", 
                            unique=True)
    
    class Meta:
        verbose_name = "二级分类"
        verbose_name_plural = "二级分类"
        
    def __str__(self):
        return self.text


class Articles(models.Model):
    """文章"""
    title = models.CharField(max_length=80, verbose_name="标题", unique=True)
    #text = models.TextField(verbose_name="内容")
    text = MDTextField(verbose_name="文章内容")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="发布日期",
                                    editable=False)
    modify_date = models.DateTimeField(default=timezone.now,
                                       verbose_name="修改日期",
                                       editable=False)
    # 分类
    meta_top = models.ForeignKey(TopMetas, models.SET_DEFAULT,default=1,
                                 verbose_name="一级分类",
                                 related_name="meta_top")
    meta_second = models.ForeignKey(SecondMetas, models.SET_DEFAULT,default=1,
                                    verbose_name="二级分类",
                                    related_name="meta_second")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="作者",
                               on_delete=models.CASCADE)
    read_times = models.IntegerField(verbose_name="阅读次数", editable=False,
                                     default=0)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                   related_name="like", verbose_name="点赞数",
                                   editable=False)
    public = models.BooleanField(default=True, verbose_name="是否公开")
    

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = "文章"

    def getMarkdownContent(self):
        """将markdown转为html"""
        return markdown.markdown(self.text, extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])

    def getHTML(self):
        """将markdown转为html,并支持emoji"""
        tmp = emojize(self.text, language='alias')
        tmp = re.sub(r':fa-(\w+):', r'<i class="fas fa-\1"></i>', tmp)
        tmp = re.sub(r':tw-(\w+):', r'<img src="https://cdnjs.cloudflare.com/ajax/libs/twemoji/2.0.0/16x16/\1.png" class="twemo" alt="twemoji图片"></i>', tmp)
        tmp = markdown.markdown(tmp, extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
            
        ])
        return tmp
        
    def getFirstImage(self):
        """获取文章第一张图片"""
        PATTERN = r'<img.*?src=\"(.*?)\".*?>'
        html = self.getMarkdownContent()
        result = re.findall(PATTERN, html, flags=re.S)
        if len(result) == 0:
            return "https://fakeimg.pl/250x200/"
        else:
            return result[0]
    
    def getBrief(self):
        """获取文章摘要"""
        return strip_tags(self.getMarkdownContent())[:140]
    
    def __str__(self):
        return self.title
