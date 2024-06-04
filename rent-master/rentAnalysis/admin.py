from django.contrib import admin
from .models import Rent

admin.site.site_title = '租房信息管理系统'
admin.site.site_header = '租房信息管理系统'

class RentAdmin(admin.ModelAdmin):
    list_display = ['title','address','area','direction','types','price','remark']
    search_fields = ['title','address','area','types','direction','price','remark']
    list_per_page = 30

admin.site.register(Rent, RentAdmin)