from django.shortcuts import render
from .models import homepage
from main_page.models import userinfo
from django.http import HttpResponseNotFound
# Create your views here.

def homepage_show(request,name):
    if request.user.username==name:
        page = homepage.objects.get(owner__user__username=name)
        return render(request,'my_page/mypage.html',{'PAGE':page})
    return HttpResponseNotFound(request.user.username)
