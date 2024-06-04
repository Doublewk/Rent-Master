from django.urls import re_path as url
from . import views
app_name = 'app'
urlpatterns = [
    url(r'^$', views.index),
    url('首页', views.index, name='index'),
    url('搜索', views.search, name='search'),
    url('整租', views.entire_rent, name='entire_rent'),
    url('合租', views.share_rent, name='share_rent'),
    url('leave_a_message', views.leave_a_message, name='leave_a_message'),
    url('Large_Language_Model', views.Large_Language_Model, name='Large_Language_Model'),
    ]