# from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from .models import Leave_a_message
from django.core.paginator import Paginator
from rentAnalysis.models import Rent
from .utils import get_page_range, main, get_access_token

def leave_a_message(request):
    method = request.method
    if method == "GET":
        return render(request, "./app/leave_a_message.html")
    elif method == "POST":
        content = request.POST.get("content")
        username = request.POST.get("username")
        print(content,username)
        try:
            new_post = Leave_a_message(username=username,content=content)
            print(1)
            new_post.save()
            result1 = "你已留言成功，感谢你的留言"
            result2 = "继续留言"
            return render(request, "./app/leave_a_message.html", context={
                "result1": result1,"result2": result2})
        except Exception:
            result3 = "输入异常，请重新留言留言"
            result4 = "继续留言"
            return render(request, "./app/leave_a_message.html", context={
                "result1": result3, "result2": result4})

def Large_Language_Model(request):
    method = request.method
    if method == "GET":
        return render(request, "app/Large_Language_Model.html")
    elif method == "POST":
        keyword = request.POST.get("keyword")
        try:
            content = main(keyword)
            result1 = "搜索结果为："
            result2 = content
            result3 = "重新搜索"
            return render(request, "app/Large_Language_Model.html", context={
                "result1": result1, "result2": result2,"result3": result3})
        except Exception:
            result1 = "输入错误，请重新输入"
            result3 = "重新搜索"
            return render(request, "app/Large_Language_Model.html", context={
                "result1": result1, "result3": result3})



def search(request):
    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        house_get = Rent.objects.filter(Q(title__contains=keyword)) | Rent.objects.filter(Q(price__contains=keyword)) \
                    | Rent.objects.filter(Q(address__contains=keyword)) | Rent.objects.filter(Q(district__contains=keyword))
        if house_get:
            count = len(house_get)
            paginator = Paginator(house_get, 30)
            current_page_num = int(request.GET.get("page", 1))
            list = get_page_range(paginator, current_page_num)
            page_range = list[0]
            current_page = list[1]
            return render(request,"app/house_search.html",locals())
        else:
            notfound = '没找到...  试试查找别的区域或小区吧（‐＾▽＾‐）'
            return render(request,"app/house_search.html",{'notfound':notfound})
    else:
        notfound = '请输入区域或小区名...'
        return render(request,"app/house_search.html",{'notfound':notfound})




def index(request):
    rent_list = Rent.objects.all()
    count = len(rent_list)
    paginator = Paginator(rent_list, 30)
    current_page_num = int(request.GET.get("page", 1))
    list = get_page_range(paginator, current_page_num)
    page_range = list[0]
    current_page = list[1]
    return render(request,"app/index.html",locals())


def entire_rent(request):
    keyword = "整租"
    rent_list = Rent.objects.filter(Q(title__contains=keyword))
    count = len(rent_list)
    paginator = Paginator(rent_list, 30)
    current_page_num = int(request.GET.get("page", 1))
    list = get_page_range(paginator, current_page_num)
    page_range = list[0]
    current_page = list[1]
    return render(request,"app/entire_rent.html",locals())

def share_rent(request):
    keyword = "合租"
    rent_list = Rent.objects.filter(Q(title__contains=keyword))
    count = len(rent_list)
    paginator = Paginator(rent_list, 30)
    current_page_num = int(request.GET.get("page", 1))
    list = get_page_range(paginator, current_page_num)
    page_range = list[0]
    current_page = list[1]
    return render(request,"app/share_rent.html",locals())

