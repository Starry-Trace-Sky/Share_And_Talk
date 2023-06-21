"""为app users定义URL模式"""
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

from . import viewConfig
from . import views


app_name = 'users'
urlpatterns = [
    # 登录页面
    path('login/', views.CustomLoginView.as_view(), name='login'),
    # 注册页面
    path('register/', views.register, name='register'),
    # 包含默认的身份验证URL
    path('', include('django.contrib.auth.urls')),
    # 用户配置
    path('profile/', viewConfig.index, name='userProfile')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
