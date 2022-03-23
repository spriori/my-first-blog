from pipes import Template
from unicodedata import name
from django.urls import path

from blog.models import Edited_by, Post
from . import views
from django.views.generic import TemplateView

from blog.views import PostDetail, PostEdit, PostList, PostNew, ModifiedList

urlpatterns = [
    path('', PostList.as_view(model=Post), name='post_list'),
    path('post/<int:pk>/', PostDetail.as_view(model=Post), name='post_detail'),
    path('post/new', PostNew.as_view(model=Post), name='post_new'),
    path('post/<int:pk>/edit/', PostEdit.as_view(model=Post), name='post_edit'),
    path('post/<int:pk>/modified_list', ModifiedList.as_view(model=Edited_by), name='modified_list')
]