# encoding: utf-8

import xadmin
from .models import Article, ArticleCategory, ArticleTag


class ArticleCategoryAdmin(object):
    list_display = ["name", "add_time"]
    list_filter = ["add_time",]
    search_fields = ['name', ]


class ArticleTagAdmin(object):
    list_display = ["name", "add_time"]
    list_filter = ["add_time", ]
    search_fields = ['name', ]


class ArticleAdmin(object):
    list_display = ["title", "category", "user", "click_number", "comment_number", "favor_number", "word_count",
                     "brief", "add_time"]
    search_fields = ['title', 'brief']
    list_editable = ['title', "click_number", "comment_number", "favor_number", "word_count"]
    list_filter = ["click_number", "comment_number", "favor_number", "word_count",  "add_time", "category__name"]
    style_fields = {"content": "ueditor"}


xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(ArticleCategory, ArticleCategoryAdmin)
xadmin.site.register(ArticleTag, ArticleTagAdmin)
