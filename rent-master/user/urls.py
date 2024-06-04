from django.urls import path
from .views import login,register,set_password

app_name = 'user'

urlpatterns = [
    path('login', login, name="login"),
    path('register', register, name="register"),
    path('set_password', set_password, name="set_password"),
]