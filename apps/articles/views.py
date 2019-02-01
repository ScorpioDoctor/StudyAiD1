from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters

from .models import Article, ArticleCategory
from .serializers import ArticleSerializer, ArticleCategorySerializer
from .filters import ArticleFilter


class ArticleListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'pg'
    max_page_size = 100


class ArticleListView0(APIView):
    """
    List all articles, or create a new article.
    """
    def get(self, request, format=None):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)


class ArticleListView1(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ArticleListView2(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = ArticleListPagination


from rest_framework import viewsets


class ArticleListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    文章列表页, 分页， 搜索， 过滤， 排序
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = ArticleListPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = ArticleFilter
    search_fields = ('title', 'brief', 'content')
    ordering_fields = ('click_number', 'favor_number', 'comment_number', 'word_count', 'add_time')


class ArticleCategoryListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    文章类别列表页
    """
    queryset = ArticleCategory.objects.all()
    serializer_class = ArticleCategorySerializer