from django.contrib import admin
from .models import Leave_a_message
class RentAdmin(admin.ModelAdmin):
    list_display = ['id','content','add_date']
    search_fields = ['id']
    list_per_page = 30

admin.site.register(Leave_a_message, RentAdmin)