# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib.auth.models import User

class userinfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    college = models.CharField(max_length=32)
    department = models.CharField(max_length=32)
    classinfo = models.CharField(max_length=32)
    photo = models.ImageField(upload_to='upload_imag/', default='upload_imag/default.png')
    signature = models.CharField(max_length=256,default='Hello World!')
    objects = models.Manager()
    def __str__(self):
        return '%s (%s)' %(self.name,self.user.username)


class post(models.Model):
    title =  models.CharField(max_length=64)
    summary = models.CharField(max_length=256,blank=True)
    category = models.ForeignKey('category',on_delete=models.CASCADE)
    content =  models.TextField()
    view_count = models.IntegerField()
    comment_count = models.IntegerField()
    author = models.ForeignKey('userinfo',on_delete=models.CASCADE)
    ranking = models.IntegerField()
    publish_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    def __str__(self):
        return self.title

class post_like(models.Model):
    post = models.ForeignKey(post,on_delete=models.CASCADE)
    like_user = models.ForeignKey(userinfo,on_delete=models.CASCADE)
    like_time = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    def __str__(self):
        return self.post.title+"_"+self.like_user.user.username

class post_like_count(models.Model):
    post = models.OneToOneField(post,on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    objects = models.Manager()
    def __str__(self):
        return self.post.title

class post_tag(models.Model):
    tag_name = models.CharField(max_length=16)
    posts = models.ManyToManyField(post)
    objects = models.Manager()
    def __str__(self):
        return self.tag_name

class category(models.Model):
    name = models.CharField(max_length=32,unique=True)
    admin = models.ForeignKey('userinfo',on_delete=models.CASCADE)
    objects = models.Manager()
    def __str__(self):
        return self.name
