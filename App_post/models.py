from typing import Tuple
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Blog(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_author')
    blog_title = models.CharField(verbose_name='Blog Title', max_length=264)
    blog = models.TextField(verbose_name='Put your mind',)
    blog_img = models.ImageField(upload_to='post_images',verbose_name='Blog Image')
    slug = models.SlugField(max_length=100,unique=True)
    publich_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    class Meta:
        ordering =['-publich_date',]

    def __str__(self):
        return self.blog_title

class comment(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='blog_comment')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_comment')
    comment = models.TextField()
    comment_date = models.DateField(auto_now_add=True)
    class Meta:
        ordering = ['-comment_date',]
    def __str__(self):
        return self.comment

class like(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='blog_like')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_like')
    def __str__(self):
        return self.user