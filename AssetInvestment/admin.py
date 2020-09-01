from django.contrib import admin

# Register your models here.
from .models import Portfolio, Asset, tData, User


class PortfolioAdmin(admin.ModelAdmin):
    #列表页属性
    list_display = ['pk', 'pname', 'pnum']
    list_filter = ['pnum']
    search_fields = ['pname']
    list_per_page = 5


class AssetAdmin(admin.ModelAdmin):
    #显示改得更好看
    #列表页属性
    list_display = ['pk', 'aname', 'acode', 'abelong']
    list_filter = ['abelong']
    search_fields = ['aname', 'acode']
    list_per_page = 5

    #执行动作的位置
    actions_on_top = False
    actions_on_bottom = True



# 注册
admin.site.register(Portfolio,PortfolioAdmin)
admin.site.register(Asset,AssetAdmin)
admin.site.register(tData)
admin.site.register(User)
