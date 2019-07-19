from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name = 'index'),
    path('post/<int:post_id>/',views.post_show,name = 'curr_post'),
    path('category/<int:category_id>/',views.category_show,name = 'curr_category'),
    path('post_sub/', views.post_sub,name = 'post_sub'),
    path('post_creat', views.post_creat, name='post_creat'),
    path('search/',views.search,name='search_post'),
    path('like/',views.like,name = 'like'),
    path('favor/',views.favor,name = 'favor'),
    path('delete_post',views.deletePost,name = 'delete_post'),
    path('change/',views.change_data,name = 'change'),
    path('readall/',views.user_mark_all_read,name = 'user_mark_all_read')
]
