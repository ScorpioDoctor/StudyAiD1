# -*- coding: utf-8 -*-
__author__ = 'antares'

import django_filters

from .models import Article


class ArticleFilter(django_filters.rest_framework.FilterSet):
    """
    文章的过滤类
    """
    # clickmin = django_filters.NumberFilter(field_name='click_number', help_text="最低点击量", lookup_expr='gte')
    # favormin = django_filters.NumberFilter(field_name='favor_number', help_text="最低收藏量", lookup_expr='gte')
    # commentmin = django_filters.NumberFilter(field_name='comment_number', help_text="最低评论量", lookup_expr='gte')
    # wordcount_min = django_filters.NumberFilter(field_name='word_count', help_text="最少字数", lookup_expr='gte')
    # wordcount_max = django_filters.NumberFilter(field_name='word_count', help_text="最多字数", lookup_expr='lte')
    title = django_filters.CharFilter(field_name='title', help_text='按标题模糊查询', lookup_expr='icontains')

    class Meta:
        model = Article
        fields = ['category', 'tags', 'title']