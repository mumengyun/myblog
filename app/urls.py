from django.urls import path
from .views import blog, user

app_name = 'app1'
urlpatterns = [
    # ex: /blog  主页
    path('', blog.Index.as_view(), name='index'),
    # ex: /blog/detail/1  博客详情
    path('detail/<int:blog_id>/', blog.Article.as_view(), name='article'),
    # ex: /blog/category/python  分类列表
    path('category/<str:category_id>/', blog.Article_category.as_view(), name='category'),
    # ex: /blog/tag/mysql   标签文章列表
    path('tag/<str:tag_id>/', blog.Article_tag.as_view(), name='tag'),
    # ex: /blog/search?=xxx   搜索
    path('search/', blog.Search.as_view(), name='search'),
    # 用户登陆
    path('sign_in/', user.SignIn.as_view(), name='sign_in'),
    # 用户注册
    path('sign_up/', user.SignUp.as_view(), name='sign_up'),
    # 用户注销
    path('sign_out/', user.SignOut.as_view(), name='sign_out'),
]
