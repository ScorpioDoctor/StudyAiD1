"""StudyAiD1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path, include
from django.views.static import serve

from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

import xadmin

from StudyAiD1.settings import MEDIA_ROOT
from articles import views as article_views

router = DefaultRouter()

# 注册文章app相关的路由
router.register('article/list', article_views.ArticleListViewSet)
router.register('article/category/list', article_views.ArticleCategoryListViewSet)


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # 配置上传文件的访问处理函数
    re_path(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    # drf 文档
    re_path(r'^docs/', include_docs_urls(title='人工智能社区')),
    # 文章的 list 视图
    # path('articles/', article_views.ArticleListView.as_view(), name='articles-list'),
    # path('articles/', article_views.articles_list, name='articles-list'),
    # 路由集合
    path('', include(router.urls)),
]
