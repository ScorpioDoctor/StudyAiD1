import xadmin
from .models import Algorithm, AlgorithmCategory, AlgorithmCategoryBrand
from .models import Banner

class AlgorithmAdmin(object):
    list_display = ["name", "click_number", "favor_number", "brief", "is_hot", "add_time"]
    search_fields = ['name', "brief",]
    list_editable = ["is_hot", ]
    list_filter = ["click_number", "favor_number", "is_hot", "add_time", "category__name"]
    style_fields = {"description": "ueditor"}


class AlgorithmCategoryAdmin(object):
    list_display = ["name", "category_type", "parent_category", "is_tab" , "add_time"]
    list_filter = ["category_type", "parent_category", "is_tab"]
    search_fields = ['name', 'description']


class AlgorithmBrandAdmin(object):
    list_display = ["category", "image", "name", "description"]

    def get_context(self):
        context = super(AlgorithmBrandAdmin, self).get_context()
        if 'form' in context:
            context['form'].fields['category'].queryset = AlgorithmCategory.objects.filter(category_type=1)
        return context


class BannerAlgorithmAdmin(object):
    list_display = ["algorithm", "image", "index"]

xadmin.site.register(Algorithm, AlgorithmAdmin)
xadmin.site.register(AlgorithmCategory, AlgorithmCategoryAdmin)
xadmin.site.register(Banner, BannerAlgorithmAdmin)
xadmin.site.register(AlgorithmCategoryBrand, AlgorithmBrandAdmin)

