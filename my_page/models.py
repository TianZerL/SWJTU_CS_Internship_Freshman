from django.db import models
from main_page.models import userinfo,post
# Create your models here.


class homepage(models.Model):
    owner = models.OneToOneField(userinfo,on_delete=models.CASCADE)
    favorte = models.ManyToManyField(post,related_name='my_favor_post',blank=True) 
    my_posts = models.ManyToManyField(post,related_name='my_post',blank=True)
    follow = models.ManyToManyField(userinfo,related_name='follow_sb',blank=True)
    objects = models.Manager()
    def __str__(self):
        return self.owner.name