from django.contrib import admin
from .models import User
# Register your models here.
class RentAdmin(admin.ModelAdmin):
    list_display = ['username','password']
    search_fields = ['username']
admin.site.register(User, RentAdmin)