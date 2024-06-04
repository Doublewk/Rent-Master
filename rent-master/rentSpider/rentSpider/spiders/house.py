# -*- coding: utf-8 -*-
import re
import scrapy
import random
from rentSpider.items import RentspiderItem

class HouseSpider(scrapy.Spider):
    name = 'house'
    allowed_domains = ['cd.lianjia.com']
    start_urls = ['https://cd.lianjia.com/zufang/']
    proxies = {
        'http' :'http://114.231.8.26:8888',
        'https': 'https://114.231.8.26:8888',
        'http': 'http://117.71.155.126:8089',
        'https': 'https://117.71.155.126:8089',
        'http': 'http://180.122.147.205:8888',
        'https': 'https://180.122.147.205:8888',
        'http': 'http://114.232.110.33:8089',
        'https': 'https://114.232.110.33:8089',
        'http': 'http://117.69.237.252:8089',
        'https': 'https://117.69.237.252:8089',
        'http': 'http://114.231.41.190:8089',
        'https': 'https://114.231.41.190:8089',
        'http': 'http://223.215.177.0:8089',
        'https': 'https://223.215.177.0:8089',
        'http': 'http://8.142.201.136:80',
        'https': 'https://8.142.201.136:80',
    }

    def parse(self, response):
        for url in response.xpath('//*[@id="filter"]/ul[2]/li/a/@href').extract()[1:]:
            try:
                yield scrapy.Request('https://cd.lianjia.com/' + url, callback=self.page)
            except Exception:
                print("更换代理中")
                new_proxy = random.choice(list(self.proxies.values()))
                yield scrapy.Request('https://cd.lianjia.com/' + url, callback=self.page, meta = {'proxy': new_proxy})

    def page(self, response):
        page = response.xpath('//*[@id="content"]/div[1]/div[2]/@data-totalpage').extract()
        if not page:
            page = 2
        else:
            page = eval(page[0])+1
        for i in range(1, page):
            try:
                yield scrapy.Request(response.url + 'pg{}'.format(i), callback=self.detail)
            except Exception:
                print("更换代理中")
                new_proxy = random.choice(list(self.proxies.values()))
                yield scrapy.Request(response.url + 'pg{}'.format(i), callback=self.detail, meta = {'proxy': new_proxy})

    def detail(self, response):
        for div in response.xpath('//*[@id="content"]/div[1]/div[1]/div'):
            item = RentspiderItem()
            item['title'] = div.xpath('./div/p[1]/a/text()').extract()[0].strip()
            item['district'] = response.xpath('//*[@id="content"]/div[1]/p/a[2]/text()').extract()[0].strip("租房")
            item['link'] = 'https://cd.lianjia.com'+div.xpath('./div/p[1]/a/@href').extract()[0].strip()
            item['picture'] = div.xpath('./a/img/@data-src').extract()[0]
            list1 = div.xpath('./div/p[2]//text()').extract()
            list2 = ''.join(list1).strip().replace("/","").split()
            if len(list2) == 6:
                item['address'] =list2[0]
                if "㎡" not in list2[1]:
                    print("不符合要求")
                    pass
                else:
                    item['area'] = list2[1].replace('㎡', '')
                item['direction'] = list2[2]
                item['types'] = list2[3]
                item['floor'] = (list2[4]+list2[5])
                item['price'] = div.xpath('./div/span/em/text()').extract()[0]
                list4 = div.xpath('./div/p[3]//text()').extract()
                item['remark'] = ''.join([item.strip()+" " for item in list4]).strip()
                yield item
            else:
                print("不符合要求")
                pass

