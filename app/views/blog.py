from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models.aggregates import Count
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from ..models import *


# Create your views here.


def paginator(article, page_num):
    """分页相关数据函数"""
    paginator_num = Paginator(article, 5)  # 每页数目
    page_range = paginator_num.page_range  # 分页迭代
    page_next = paginator_num.num_pages  # 分页总数
    page_list = paginator_num.page(page_num)  # 每页数据
    paginator_data = {
        'page_list': page_list,
        'page_range': page_range,
        'page_next': page_next
    }
    return paginator_data


def hot():
    """热门文章/标签云/分类数据"""
    category_list = Category.objects.all()
    hot_list = Blog.objects.all().order_by('-view_num')[:5]
    tag_list = Tag.objects.annotate(blog_num=Count('blog'))

    public_data = {
        'category_list': category_list,
        'hot_list': hot_list,
        'tag_list': tag_list
    }
    return public_data


class Index(View):
    """首页页面"""

    def get(self, request):
        blog_list = Blog.objects.all().order_by('-create_time')
        page_num = int(request.GET.get('page_num', '1'))
        paginator_data = paginator(blog_list, page_num)

        # 热门文章数据
        public_data = hot()

        data = {
            'blog_list': blog_list,
            'paginator_data': paginator_data,
            'public_data': public_data
        }
        return render(request, 'index.html', context=data)


class Article(View):
    """博客详情页面"""

    def get(self, request, blog_id):
        article = Blog.objects.get(pk=blog_id)

        # 点赞数
        if request.GET.get('like'):
            like_status = request.GET.get('like')
        else:
            like_status = 0
        article.like_num += int(like_status)
        article.save()

        # 阅读数
        article.view_num += 1
        article.save()

        # 热门文章数据
        public_data = hot()

        data = {
            'article_data': article,
            'public_data': public_data
        }
        return render(request, 'article.html', context=data)


class Article_category(View):
    """分类"""

    def get(self, request, category_id):
        blog_list = Blog.objects.filter(category__name=category_id).order_by('-create_time')
        articles_total = blog_list.count()
        page_num = int(request.GET.get('page_num', '1'))
        paginator_data = paginator(blog_list, page_num)

        # 热门文章数据
        public_data = hot()

        data = {
            'article_data': blog_list,
            'paginator_data': paginator_data,
            'articles_total': articles_total,
            'public_data': public_data
        }

        return render(request, 'category.html', context=data)


class Article_tag(View):
    """根据tag标签分类的文章"""

    def get(self, request, tag_id):
        blog_list = Blog.objects.filter(tags__name=tag_id)
        page_num = int(request.GET.get('page_num', '1'))
        paginator_data = paginator(blog_list, page_num)
        tag_id = tag_id
        public_data = hot()

        data = {
            'article_data': blog_list,
            'paginator_data': paginator_data,
            'public_data': public_data,
            'tag_id': tag_id
        }

        return render(request, 'tag.html', context=data)


class Search(View):
    """搜索"""

    def get(self, request):
        search_text = request.GET.get('key')
        blog_list = Blog.objects.filter(Q(title__icontains=search_text) | Q(content__icontains=search_text)).order_by(
            '-create_time')
        articles_total = blog_list.count()
        page_num = int(request.GET.get('page_num', '1'))
        paginator_data = paginator(blog_list, page_num)

        # 热门文章数据
        public_data = hot()

        data = {
            'paginator_data': paginator_data,
            'search_text': search_text,
            'articles_total': articles_total,
            'public_data': public_data
        }

        return render(request, 'search.html', context=data)
