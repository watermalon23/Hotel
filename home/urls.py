from .views import*
from django.urls import path
from home import views


urlpatterns = [
    path('api/get_hotel/',get_hotel),
    path("",views.index,name="home"),
    path("login.html",views.user,name="login"),
    path("create_acc.html",views.create_acc,name="create_acc"),
    path("signin.html",views.signin,name="signin"),
]
