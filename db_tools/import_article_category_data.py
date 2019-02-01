# -*- coding: utf-8 -*-
__author__ = 'antares'
import sys
import os


pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+"../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "StudyAiD1.settings")

import django
django.setup()

from algorithms.models import AlgorithmCategory
from articles.models import ArticleCategory, ArticleTag

# 拿到所有算法的二级类目作为文章的类别
categories = AlgorithmCategory.objects.filter(category_type=2)

# 拿到所有算法的三级类目作为文章的标签
tags = AlgorithmCategory.objects.filter(category_type=3)

for cat in categories:
    art_cat = ArticleCategory()
    art_cat.name = cat.name
    # art_cat.save()
    print(art_cat.name)

for tag in tags:
    art_tag = ArticleTag()
    art_tag.name = tag.name
    # art_tag.save()
    print(art_tag.name)