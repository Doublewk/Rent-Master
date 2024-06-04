import hashlib
from django.shortcuts import render
from .models import User
from django.conf import settings

# Create your views here.
def register(request):
    method = request.method # 请求方法
    if method == "GET":
        return render(request, "./user/register.html")
    elif method == "POST":
        username = request.POST.get("username")
        res = User.objects.filter(username=username)
        """验证用户名是否存在"""
        if res:
            result1 = "sorry,用户名已被注册，请尝试新的用户名"
            result2 = "重新注册"
            result3 = "register"
            return render(request, "./user/register.html", context={
                "result1": result1, "result2": result2,"result3": result3})

        """密码加密"""
        password = request.POST.get("password")
        res = password + settings.SECRET_KEY
        password = hashlib.md5(res.encode("utf-8")).hexdigest()
        email = request.POST.get("email")
        """添加数据"""
        User.objects.create(username=username, password=password, email=email)
        result1 = "恭喜，注册成功！"
        result2 = "前往登录"
        result3 = "login"
        return render(request, "./user/register.html", context={
            "result1": result1, "result2": result2,"result3": result3})

def login(request):
    method = request.method
    if method == "GET":
        return render(request, "./user/login.html")
    elif method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = User.objects.get(username=username)
            res = password + settings.SECRET_KEY
            password = hashlib.md5(res.encode("utf-8")).hexdigest()
            if password == user.password:
                username = ":" + username
                return render(request, "./app/index.html", context={
                    "username": username
                })
            else:
                result1 = "sorry,密码错误，请重新输入密码"
                result2 = "重新登陆"
                return render(request, "./user/login.html",context={
                    "result1": result1,"result2":result2})
        except User.DoesNotExist:
            result1 = "sorry,用户名不存在"
            result2 = "重新登陆"
            return render(request, "./user/login.html", context={
                "result1": result1,"result2":result2})


def set_password(request):
    method = request.method # 请求方法
    if method == "GET":
        return render(request, "./user/set_password.html")
    elif method == "POST":
        username = request.POST.get('username')
        old_password = request.POST.get('password')
        new_password = request.POST.get('set_password')
        old_res = old_password + settings.SECRET_KEY
        old_password_encryption = hashlib.md5(old_res.encode("utf-8")).hexdigest()
        new_res = new_password + settings.SECRET_KEY
        new_password_encryption = hashlib.md5(new_res.encode("utf-8")).hexdigest()
        try:
            user = User.objects.get(username=username)
            if old_password_encryption == user.password:
                User.objects.filter(username=username).update(password = new_password_encryption)
                result1 = '密码修改成功'
                return render(request, './user/set_password.html', context={"result1": result1})
            else:
                result1 = '旧密码错误'
                return render(request, './user/set_password.html', context={"result1": result1})
        except User.DoesNotExist:
            result1 = '用户不存在'
            return render(request, './user/set_password.html', context={"result1": result1})

