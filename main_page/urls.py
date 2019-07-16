from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name = 'index'),
    path('post/<int:post_id>/',views.post_show,name = 'curr_post'),
    path('category/<int:category_id>/',views.category_show,name = 'curr_category'),
    path('post_sub/', views.post_sub,name = 'post_sub'),
    path('search/',views.search,name='search_post')
]
