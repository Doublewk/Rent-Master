from django.urls import path
from .views import home,  index, handle_district1, handle_district2,\
handle_district3, handle_district4,handle_district5, handle_district6,\
handle_district7, handle_district8,handle_district9, handle_district10,\
handle_district11, handle_district12,handle_district13, handle_district14,\
handle_district15, handle_district16,handle_district17, handle_district18,\
handle_district19, handle_district20,handle_district21, handle_district22,\
handle_district23,handle_district24, district1, district2,\
district3, district4,district5, district6,district7, district8,\
district9, district10,district11, district12,district13, district14,\
district15, district16,district17, district18,district19, district20,\
district21, district22, district23, district24, liner
app_name = 'rentAnalysis'

urlpatterns = [
    path('主页', home, name='home'),
    path('index/', index, name='index'),
    path('liner', liner, name='liner'),
    path('锦江/district', handle_district1, name='district1/district'),
    path('青羊/district', handle_district2, name='district2/district'),
    path('武侯/district', handle_district3, name='district3/district'),
    path('高新/district', handle_district4, name='district4/district'),
    path('成华/district', handle_district5, name='district5/district'),
    path('金牛/district', handle_district6, name='district6/district'),
    path('天府新区/district', handle_district7, name='district7/district'),
    path('高新西/district', handle_district8, name='district8/district'),
    path('双流/district', handle_district9, name='district9/district'),
    path('温江/district', handle_district10, name='district10/district'),
    path('郫都/district', handle_district11, name='district11/district'),
    path('龙泉驿/district', handle_district12, name='district12/district'),
    path('新都/district', handle_district13, name='district13/district'),
    path('天府新区南区/district', handle_district14, name='district14/district'),
    path('青白江/district', handle_district15, name='district15/district'),
    path('都江堰/district', handle_district16, name='district16/district'),
    path('彭州/district', handle_district17, name='district17/district'),
    path('简阳/district', handle_district18, name='district18/district'),
    path('新津/district', handle_district19, name='district19/district'),
    path('崇州/district', handle_district20, name='district20/district'),
    path('大邑/district', handle_district21, name='district21/district'),
    path('金堂/district', handle_district22, name='district22/district'),
    path('蒲江/district', handle_district23, name='district23/district'),
    path('邛崃/district', handle_district24, name='district24/district'),

    path('锦江/', district1, name='district1'),
    path('青羊/', district2, name='district2'),
    path('武侯/', district3, name='district3'),
    path('高新/', district4, name='district4'),
    path('成华/', district5, name='district5'),
    path('金牛/', district6, name='district6'),
    path('天府新区/', district7, name='district7'),
    path('高新西/', district8, name='district8'),
    path('双流/', district9, name='district9'),
    path('温江/', district10, name='district10'),
    path('郫都/', district11, name='district11'),
    path('龙泉驿/', district12, name='district12'),
    path('新都/', district13, name='district13'),
    path('天府新区南区/', district14, name='district14'),
    path('青白江/', district15, name='district15'),
    path('都江堰/', district16, name='district16'),
    path('彭州/', district17, name='district17'),
    path('简阳/', district18, name='district18'),
    path('新津/', district19, name='district19'),
    path('崇州/', district20, name='district20'),
    path('大邑/', district21, name='district21'),
    path('金堂/', district22, name='district22'),
    path('蒲江/', district23, name='district23'),
    path('邛崃/', district24, name='district24'),
]