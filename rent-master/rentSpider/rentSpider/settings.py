
import os
import sys
import django

sys.path.append(os.path.dirname(os.path.abspath('.')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rent.settings')  # Django Project Name
django.setup()

BOT_NAME = 'rentSpider'

SPIDER_MODULES = ['rentSpider.spiders']
NEWSPIDER_MODULE = 'rentSpider.spiders'


USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'


ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
   'rentSpider.pipelines.RentspiderPipeline': 300,  # Pipeline receives content
}

