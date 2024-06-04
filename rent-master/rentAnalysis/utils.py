import re
from .models import Rent
from django.db.models import  Count

def num(s):
    number1 = re.findall(r'\d+', s)
    numbers = ''.join(number1)
    return numbers

def is_number(s):
    pattern = r'^\d+(\.\d+)?$'
    return bool(re.match(pattern, s))
def handle_districts(request, district):
    data = []
    data1 = []
    data2 = []
    data3 = ""
    data4 = ""
    rent = Rent.objects.filter(district=district)
    types_data = rent.values('types').annotate(count=Count('types'))
    # from pyspark.sql import SparkSession
    # # 创建SparkSession
    # spark = SparkSession.builder \
    #     .appName("rentSpider") \
    #     .getOrCreate()
    # area_data = rent.values_list('area', flat=True)
    # lt = [{'id': i, 'area': eval(area)} for i, area in enumerate(area_data) if is_number(area)]
    # item = {}
    # df = spark.createDataFrame(lt)
    # item['0-50'] = df.filter(df.price >= 0).filter(df.price < 50).count()
    # item['50-100'] = df.filter(df.price >= 50).filter(df.price < 100).count()
    # item['100-150'] = df.filter(df.price >= 100).filter(df.price < 150).count()
    # item['150+'] = df.filter(df.price >= 150).count()
    # print(item)
    # spark.stop()
    # print("结束spark分析")
    area_data = rent.values_list('area', flat=True)
    areas = [area for area in area_data if is_number(area)]
    classified_areas = {
        '0-50': len([area for area in areas if 0 <= eval(area) < 50]),
        '50-100': len([area for area in areas if 50 <= eval(area)  < 100]),
        '100-150': len([area for area in areas if 100 <= eval(area)  < 150]),
        '150+': len([area for area in areas if eval(area)  >= 150])
    }
    for i in types_data:
        data1.append({"value":i["count"],"name":i["types"]})
        data4 += f"房屋户型为{i['types']}有{i['count']}间房屋;<br>"
    for key in classified_areas.keys():
        data2.append({"value":classified_areas[key],"name":key})
        data3 += f"房屋面积为{key}㎡之间有{classified_areas[key]}间房屋;<br>"
    data.append(data1)
    data.append(data2)
    data.append(data3)
    data.append(data4)
    return data
