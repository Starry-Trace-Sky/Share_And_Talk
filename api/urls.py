"""Api app url pattern"""
from django.urls import path, include

from . import views


app_name = 'api'
urlpatterns = [
    # Sync qq avatar
    path('qq_photo/', views.qqPhoto, name='qqPhoto'),
    # Sync gravatar
    path('g_photo/', views.gravatarPhoto, name='GravatarPhoto'),
    # Send email
    path('send_email/', views.sendEmail, name='send_email'),
    # Like
    path('like_article/', views.like, name='like'),
    # Backup database
    path('backup_data/', views.backupDB, name='backup')
]
