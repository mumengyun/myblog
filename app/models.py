from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    """用户信息"""

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Category(models.Model):
    """博客分类"""
    name = models.CharField(verbose_name='博客分类', max_length=15)
    create_time = models.DateField(verbose_name='创建时间', auto_now_add=True)
    change_time = models.DateField(verbose_name='修改时间', auto_now=True)

    class Meta:
        verbose_name = '博客分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(verbose_name='标签', max_length=15)
    create_time = models.DateField(verbose_name='创建时间', auto_now_add=True)
    change_time = models.DateField(verbose_name='修改时间', auto_now=True)

    class Meta:
        verbose_name = '博客标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=30, verbose_name='博客标题')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    content = models.TextField(verbose_name='内容')
    create_time = models.DateField(auto_now_add=True, verbose_name='创建时间')
    change_time = models.DateField(auto_now=True, verbose_name='修改时间')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='文章分类')
    tags = models.ManyToManyField(Tag)
    view_num = models.IntegerField(default=0, verbose_name='阅读')
    like_num = models.IntegerField(default=0, verbose_name='点赞')

    class Meta:
        verbose_name = '博客文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
