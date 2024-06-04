import scrapy
from scrapy_djangoitem import DjangoItem
from rentAnalysis.models import Rent

class RentspiderItem(DjangoItem):
    django_model = Rent
