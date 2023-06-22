"""Api app url pattern"""
from django.urls import path

from . import views
from .userApi.qqAvatar import QQAvatar
from .userApi.gravatarApi import GravatarSync
from .commentApi.AddAPI import AddComment
from .commentApi.QueryAPI import QueryComment
from .commentApi.DelAPI import DelComment
from .commentApi.ModifyAPI import ModifyComment
from .commentApi.LikeAPI import LikeComment

app_name = 'api'
urlpatterns = [
    # Sync qq avatar
    path('qq_photo/', QQAvatar.as_view(), name='qqPhoto'),
    # Sync gravatar
    path('g_photo/', GravatarSync.as_view(), name='GravatarPhoto'),
    # Send email
    path('send_email/', views.sendEmail, name='send_email'),
    # Like
    path('like_article/', views.like, name='like'),
    # Backup database
    path('backup_data/', views.backupDB, name='backup')
]
# 文章评论api
urlpatterns += [
    path('query_comment/', QueryComment.as_view(), name='QueryComment'),
    path('add_comment/', AddComment.as_view(), name='AddComment'),
    path('edit_comment/', ModifyComment.as_view(), name='ModifyComment'),
    path('del_comment/', DelComment.as_view(), name='DelComment'),
    path('like_comment/', LikeComment.as_view(), name='LikeComment')
]
