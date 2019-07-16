from django.contrib import admin
from main_page import models
# Register your models here.

class post_show(admin.ModelAdmin):
    list_display = ('title','summary','author','view_count','comment_count','publish_date','modify_date')
    list_filter = ('publish_date','view_count')
    search_fields = ('title','author__name')

admin.site.register(models.userinfo)
admin.site.register(models.post,post_show)
admin.site.register(models.category)
admin.site.register(models.post_tag)
admin.site.register(models.post_like)
admin.site.register(models.post_like_count)