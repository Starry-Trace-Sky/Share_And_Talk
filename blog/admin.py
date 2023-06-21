from django.contrib import admin
from .models import TopMetas, Articles, SecondMetas


admin.site.register(TopMetas)
admin.site.register(SecondMetas)
admin.site.register(Articles)
# 设置后台名称
admin.site.site_header = 'Share And Talk后台管理'
admin.site.site_title = 'Share And Talk后台管理'
admin.site.index_title = 'Share And Talk后台管理'
