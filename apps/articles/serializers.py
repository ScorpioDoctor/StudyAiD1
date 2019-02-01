from rest_framework import serializers

from .models import Article, ArticleCategory


class ArticleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleCategory
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    category = ArticleCategorySerializer()
    class Meta:
        model = Article
        fields = "__all__"
