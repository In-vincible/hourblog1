# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template.defaultfilters import slugify

from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import URLValidator

# Create your models here.
class Author(models.Model):
    authorId=models.AutoField(primary_key=True)
    authorName=models.CharField(max_length=100)
    aboutAuthor=models.TextField()
    def __str__(self):
        return self.authorName

class Category(models.Model):
    categoryId=models.AutoField(primary_key=True)
    categoryTitle=models.CharField(max_length=100)
    slug=models.SlugField(null=True)
    def save(self, *args, **kwargs):
        self.slug=slugify(self.categoryTitle)
        super(Category, self).save(*args, **kwargs)
    def __str__(self):
        return self.categoryTitle

class Tag(models.Model):
    tagId=models.AutoField(primary_key=True)
    tagTitle=models.CharField(max_length=100)
    slug=models.SlugField(null=True)
    def save(self, *args, **kwargs):
        self.slug=slugify(self.tagTitle)
        super(Tag, self).save(*args, **kwargs)
    def __str__(self):
        return self.tagTitle

class Post(models.Model):
    postId = models.AutoField(primary_key=True)
    postTitle = models.CharField(max_length=500)
    gist = models.CharField(max_length=1000, blank=True, null=True)
    content = RichTextField()
    author = models.ForeignKey(Author)
    viewCount = models.IntegerField(default = 0)
    timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)
    tag=models.ManyToManyField(Tag)
    slug=models.SlugField(null=True)
    category=models.ManyToManyField(Category)
    titleImage= models.TextField(validators=[URLValidator()], blank=True, null=True)
    def save(self, *args, **kwargs):
        self.slug=slugify(self.postTitle)
        super(Post, self).save(*args, **kwargs)
    def __str__(self):
        return self.postTitle
