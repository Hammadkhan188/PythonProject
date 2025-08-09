from .import views
from django.urls import path,include

urlpatterns = [
    path('', views.Index,name="index"),
    path('a', views.About,name="about"),
    path('c', views.Contact,name="contact"),

]