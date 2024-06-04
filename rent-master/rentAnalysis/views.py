import json
import requests
import pandas as pd
import statsmodels.api as sm
from django.shortcuts import render
from .models import Rent
from django.db.models import Avg, Count
from django.http import HttpResponse
from django.db.models import Q
from sklearn.linear_model import LinearRegression
from .utils import handle_districts, is_number, num



def home(request):
    return render(request, 'rentAnalysis/index.html')

def index(request):
    data1 = ""
    data2 = ""
    floors = ['低楼层', '中楼层', '高楼层', '总体']
    source = [['floors','低楼层', '中楼层', '高楼层', '总体']]
    numbers = []
    results = Rent.objects.values_list('district', flat=True)
    districts = list(set(results))
    # 每个区域 楼层类型 平均单价
    for district in districts:
        temp = [district]
        rent = Rent.objects.filter(district=district)
        number = rent.count()
        numbers.append(number)
        data2 += f'{district}有{number}间房屋;<br>'
        for floor in floors[0:3]:
            price_average = rent.filter(Q(floor__contains=floor)).aggregate(Avg('price'))
            if price_average['price__avg'] == None:
                temp.append(price_average['price__avg'])
                data1 += f"{district}没有{floor}房屋;"
            else:
                temp.append(int(price_average['price__avg']))
                data1 += f"{district}{floor}房屋平均价格为{int(price_average['price__avg'])}元/月;"
        total_price_average = rent.aggregate(Avg('price'))
        if total_price_average['price__avg'] == None:
            temp.append(total_price_average['price__avg'])
            data1 += f"{district}没有房屋;<br>"
        else:
            temp.append(int(total_price_average['price__avg']))
            data1 += f"{district}房屋平均价格为{int(total_price_average['price__avg'])}元/月;<br>"
        source.append(temp)
    return HttpResponse(json.dumps({'source': source, 'districts': districts, 'number': numbers, 'avg_price': data1, 'count': data2}))

def liner(request):
    method = request.method
    if method == "GET":
        return render(request, "./rentAnalysis/liner.html")
    elif method == "POST":
        area = request.POST.get("area")
        floor = request.POST.get("floor")
        select_data = Rent.objects.values('area', 'types', 'floor', 'price')
        data_1 = []
        for i in select_data:
            if is_number(i['area']):
                num3 = eval(num(i['floor']))
                lt = [eval(i['area']), num3, i['price']]
                data_1.append(lt)
        df = pd.DataFrame(data_1, columns=['Area', 'Floor', 'Price'])
        X = df[['Area', 'Floor']]
        Y = df['Price']
        regr = LinearRegression()
        regr.fit(X, Y)
        k_lt = regr.coef_
        b = regr.intercept_
        k1 = k_lt[0]
        k2 = k_lt[1]
        print(k_lt,b)
        result1 = "多远线性回归方程为：y = {:.2f}X1+{:.2f}X2+{:.2f}".format(k1, k2, b)
        if is_number(area) and is_number(floor):
            if '-' in str(b):
                result = eval(str(k1))*eval(area)+eval(str(k2))*eval(floor)-eval(str(b).replace('-',''))
            else:
                result = eval(str(k1)) * eval(area) + eval(str(k2)) * eval(floor) + eval(str(b))
            result2 = "{}㎡，{}层的房屋租金可能为:{:.2f}元/月".format(area, floor, result)
        else:
            result2 = "输入错误，请重新输入"
        result3 = "重新咨询价格"
        # 引入线性回归模型评估相关库
        X2 = sm.add_constant(X)
        est = sm.OLS(Y, X2).fit()
        # 假设你已经执行了线性回归并得到了摘要信息
        result = est.summary()
        print("OLS回归结果:")
        print(result)
        return render(request, "./rentAnalysis/liner.html", context={
        "result1": result1, "result2": result2, "result3": result3})

def district1(request):
    return render(request, 'rentAnalysis/district.html')
def handle_district1(request):
    data = handle_districts(request,"锦江")
    return HttpResponse(json.dumps(data))
def district2(request):
    return render(request, 'rentAnalysis/district.html')
def handle_district2(request):
    data = handle_districts(request,"青羊")
    return HttpResponse(json.dumps(data))
def district3(request):
    return render(request, 'rentAnalysis/district.html')
def handle_district3(request):
    data = handle_districts(request,"武侯")
    return HttpResponse(json.dumps(data))
def district4(request):
    return render(request, 'rentAnalysis/district.html')
def handle_district4(request):
    data = handle_districts(request,"高新")
    return HttpResponse(json.dumps(data))
def district5(request):
    return render(request, 'rentAnalysis/district.html')
def handle_district5(request):
    data = handle_districts(request,"成华")
    return HttpResponse(json.dumps(data))
def district6(request):
    return render(request, 'rentAnalysis/district.html')
def handle_district6(request):
    data = handle_districts(request,"金牛")
    return HttpResponse(json.dumps(data))
def district7(request):
    return render(request, 'rentAnalysis/district.html')
def handle_district7(request):
    data = handle_districts(request,"天府新区")
    return HttpResponse(json.dumps(data))
def district8(request):
    return render(request, 'rentAnalysis/district.html')
def handle_district8(request):
    data = handle_districts(request,"高新区")
    return HttpResponse(json.dumps(data))
def district9(request):
    return render(request, 'rentAnalysis/district.html')
def handle_district9(request):
    data = handle_districts(request,"双流")
    return HttpResponse(json.dumps(data))
def district10(request):
    return render(request, 'rentAnalysis/district.html')
def handle_district10(request):
    data = handle_districts(request,"温江")
    return HttpResponse(json.dumps(data))
def district11(request):
    return render(request, 'rentAnalysis/district.html')
def handle_district11(request):
    data = handle_districts(request,"郫都")
    return HttpResponse(json.dumps(data))
def district12(request):
    return render(request, 'rentAnalysis/district.html')
def handle_district12(request):
    data = handle_districts(request,"龙泉驿")
    return HttpResponse(json.dumps(data))
def district13(request):
    return render(request, 'rentAnalysis/district.html')
def handle_district13(request):
    data = handle_districts(request,"新都")
    return HttpResponse(json.dumps(data))
def district14(request):
    return render(request, 'rentAnalysis/district.html')
def handle_district14(request):
    data = handle_districts(request,"天府新区南区")
    return HttpResponse(json.dumps(data))
def district15(request):
    return render(request, 'rentAnalysis/district.html')
def handle_district15(request):
    data = handle_districts(request,"青白江")
    return HttpResponse(json.dumps(data))
def district16(request):
    return render(request, 'rentAnalysis/district.html')
def handle_district16(request):
    data = handle_districts(request,"都江堰")
    return HttpResponse(json.dumps(data))
def district17(request):
    return render(request, 'rentAnalysis/district.html')
def handle_district17(request):
    data = handle_districts(request,"彭州")
    return HttpResponse(json.dumps(data))
def district18(request):
    return render(request, 'rentAnalysis/district.html')
def handle_district18(request):
    data = handle_districts(request,"简阳")
    return HttpResponse(json.dumps(data))
def district19(request):
    return render(request, 'rentAnalysis/district.html')
def handle_district19(request):
    data = handle_districts(request,"新津")
    return HttpResponse(json.dumps(data))
def district20(request):
    return render(request, 'rentAnalysis/district.html')
def handle_district20(request):
    data = handle_districts(request,"崇州")
    return HttpResponse(json.dumps(data))
def district21(request):
    return render(request, 'rentAnalysis/district.html')
def handle_district21(request):
    data = handle_districts(request,"大邑")
    return HttpResponse(json.dumps(data))
def district22(request):
    return render(request, 'rentAnalysis/district.html')
def handle_district22(request):
    data = handle_districts(request,"金堂")
    return HttpResponse(json.dumps(data))
def district23(request):
    return render(request, 'rentAnalysis/district.html')
def handle_district23(request):
    data = handle_districts(request,"蒲江")
    return HttpResponse(json.dumps(data))
def district24(request):
    return render(request, 'rentAnalysis/district.html')
def handle_district24(request):
    data = handle_districts(request,"邛崃")
    return HttpResponse(json.dumps(data))

