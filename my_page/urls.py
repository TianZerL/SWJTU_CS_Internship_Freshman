from django.urls import path
from . import views

urlpatterns = [
    path('<str:name>/',views.homepage_show,name = 'user_page')
]