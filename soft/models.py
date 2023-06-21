from django.db import models


class SoftMetas(models.Model):
    """软件分类"""
    text = models.CharField(max_length=20, verbose_name="软件分类名称", 
                            unique=True)
    
    class Meta:
        verbose_name = "软件分类"
        verbose_name_plural = "软件分类"
        
    def __str__(self):
        return self.text
