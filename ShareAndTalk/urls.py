"""ShareAndTalk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
import blog.views as viewws

urlpatterns = [
    # 后台管理
    path('admin/', admin.site.urls),
    # 博客
    path('', include('blog.urls')),
    # 用户
    path('users/', include('users.urls')),
    # API
    path('api/', include('api.urls')),
    # markdown插件
    path('mdeditor/', include('mdeditor.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler400 = viewws.bad_request
handler403 = viewws.permission_denied
handler404 = viewws.page_not_found
handler500 = viewws.server_error
