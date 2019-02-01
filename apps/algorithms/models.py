from datetime import datetime

from django.db import models

from DjangoUeditor.models import UEditorField


class AlgorithmCategory(models.Model):
    """
    算法类别
    """
    CATEGORY_TYPE = ((1, "一级类目"),(2, "二级类目"),(3, "三级类目"),)

    name = models.CharField(default="", max_length=30, verbose_name="类别名", help_text="类别名")
    code = models.CharField(default="", max_length=30, verbose_name="类别缩写", help_text="类别缩写")
    description = models.TextField(default="该类别暂无描述信息...", verbose_name="类别描述", help_text="类别描述")
    category_type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name="类目级别", help_text="类目级别")
    parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name="父类目级别",
                                        help_text="父目录", related_name="sub_cat", on_delete=models.CASCADE)
    is_tab = models.BooleanField(default=False, verbose_name="是否导航", help_text="是否导航")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "算法类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 某个类别被删除的时候该类别对应的所有算法都将会放到 'deleted' 这个类别下面
def get_sentinel_category():
    return AlgorithmCategory.objects.get_or_create(name='deleted', category_type=1, parent_category=None)[0]


class Algorithm(models.Model):
    """
    算法
    """
    category = models.ForeignKey(AlgorithmCategory, verbose_name="算法类目", on_delete=models.SET(get_sentinel_category))
    serial_number = models.CharField(max_length=50, default="", verbose_name="算法编号")
    name = models.CharField(max_length=100, verbose_name="算法名称")
    click_number = models.IntegerField(default=0, verbose_name="点击数")
    favor_number = models.IntegerField(default=0, verbose_name="收藏数")
    brief = models.TextField(max_length=500, verbose_name="算法简介")
    description = UEditorField(verbose_name="算法详情", imagePath="algorithm/images/",
                                  width=1000, height=300,filePath="algorithm/files/", default='')
    front_image = models.ImageField(upload_to="algorithm/images/", null=True,
                                              blank=True, verbose_name="算法封面图")
    is_hot = models.BooleanField(default=False, verbose_name="是否热门")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '算法'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Banner(models.Model):
    """
    轮播的算法
    """
    algorithm = models.ForeignKey(Algorithm, verbose_name="算法", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='banner', verbose_name="轮播图片")
    index = models.IntegerField(default=0, verbose_name="轮播顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '轮播算法'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.algorithm.name


class AlgorithmCategoryBrand(models.Model):
    """
    品牌名
    """
    category = models.ForeignKey(AlgorithmCategory, related_name='brands', null=True, blank=True,
                                 verbose_name="算法类目", on_delete=models.CASCADE)
    name = models.CharField(default="", max_length=30, verbose_name="品牌名", help_text="品牌名")
    description = models.TextField(default="", max_length=200, verbose_name="品牌描述", help_text="品牌描述")
    image = models.ImageField(max_length=200, upload_to="brands/")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "品牌"
        verbose_name_plural = verbose_name
        # db_table = "algorithm_algorithmbrand"

    def __str__(self):
        return self.name
