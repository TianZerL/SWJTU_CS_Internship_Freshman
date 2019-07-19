from django.shortcuts import render
from .models import homepage
from main_page.models import userinfo
from django.http import HttpResponseNotFound
from django_comments.signals import comment_was_posted
from django.dispatch import receiver
from notifications.signals import notify

try:
    from django.apps import apps
except ImportError:
    from django.db import models as apps

from django_comments.models import Comment
from django_comments import get_model

# Create your views here.

def homepage_show(request,name):
    if request.user.username==name:
        page = homepage.objects.get(owner__user__username=name)
        unread =request.user.notifications.unread()[:30]
        return render(request,'my_page/mypage.html',{'PAGE':page,'unread_list':unread})
    return HttpResponseNotFound(request.user.username)

@receiver(comment_was_posted, sender=Comment)
def send_message(sender, **kwargs):
    # 获取相关数据
    comment = kwargs['comment']
    request = kwargs['request']
    user = comment.user
    username = user.first_name or user.username
    
    # 获取评论的对象
    data = request.POST.copy()
    ctype = data.get("content_type")
    object_pk = data.get("object_pk")
    model = apps.get_model(*ctype.split(".", 1))
    target = model._default_manager.using(None).get(pk=object_pk)
 
    content_object = comment.content_type.get_object_for_this_type(id=object_pk)
    recipient = content_object.author.user  # 被评论时，通知文章作者
    verb = u'[%s] 评论你了' % username
    # 发送消息（level: 'success', 'info', 'warning', 'error'）
    message = {}
    message['recipient'] = recipient
    message['verb'] = verb
    message['description'] = comment.comment    # 评论详细内容
    message['target'] = target                  # 目标对象
    message['action_object'] = comment          # 评论记录
    notify.send(user, **message)