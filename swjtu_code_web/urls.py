"""swjtu_code_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.views.static import serve
from django.conf.urls.static import static
from swjtu_code_web import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('main_page.urls')),
    path('account/',include('account_page.urls')),
    path('u/',include('my_page.urls')),
    path('comments/', include('django_comments.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
