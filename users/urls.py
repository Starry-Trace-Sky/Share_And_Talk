"""为app users定义URL模式"""
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

from . import views


app_name = 'users'
urlpatterns = [
    # 包含默认的身份验证URL
    path('', include('django.contrib.auth.urls')),
    # 登录页面
    path('login/', views.CustomLoginView.as_view(), name='login'),
    # 注册页面
    path('register/', views.register, name='register'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
