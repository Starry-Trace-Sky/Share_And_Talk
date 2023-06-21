from django.urls import path, include
from . import views, viewArticle, viewMetas, viewOperateArticle
from . import viewPages, viewSearch, viewComment


app_name = 'blog'
urlpatterns = [
    # 首页
    path('', viewPages.index, name='index'),
    # 文章页面
    path('articles/<int:year>/<int:month>/<int:day>/<int:id>/', viewArticle.article, name='article'),
    # 分类
    path('metas/top/<int:id>/page/<int:pageID>/', viewMetas.metas_top, name='metas_top'),
    path('metas/second/<int:id>/page/<int:pageID>/', viewMetas.metas_second, name='metas_second'),
    path('metas/software/<int:id>/page/<int:pageID>/', viewMetas.metas_software, name='metas_software'),
    # 搜索
    path('search/', viewSearch.search, name='search'),
    
    # 增添文章
    path('new_article/', viewOperateArticle.newArticle, name='new_article'),
    # 编辑修改文章
    path('edit_article/<int:id>/', viewOperateArticle.editArticle, name='edit_article'),
    # 删除文章
    path('delete_article/<int:id>/', viewOperateArticle.deleteArticle, name='delete_article'),
    # 我的文章
    path('my_articles/', viewMetas.myArticles, name='my_articles'),
    
    # 页数
    path('pages/', viewPages.pages, name='pages'),
    # 帮助页面
    path('help/', viewArticle.help, name='articleHelp'),
    
    # 查看评论
    path('query_comment', viewComment.queryComment, name='queryComment'),
    # 添加评论
    path('add_comment/', viewComment.addComment, name='addComment'),
    # 修改评论
    path('edit_comment/', viewComment.editComment, name='editComment'),
    # 删除评论
    path('delete_comment/', viewComment.deleteComment, name='deleteComment'),

    # 404
    path('404.html', views.notFound, name='notFound'),
]
