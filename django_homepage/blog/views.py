# -*- coding:UTF-8 -*-
from django.shortcuts import render
from django.views.generic import ListView,DetailView,TemplateView
from django.views.generic.dates import ArchiveIndexView,YearArchiveView,MonthArchiveView,DayArchiveView,TodayArchiveView
from tagging.models import Tag,TaggedItem
# tagging 패키지에서 정의한 모델 클래스
from tagging.views import TaggedObjectList

from blog.models import Post

# Create your views here.

class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    # 템플릿 파일
    context_object_name = 'posts'
    # 컨텍스트 변수 이름 변경
    paginate_by = 2
    # 한 페이지당 보여줄 객체의 수

class PostDV(DetailView):
    model = Post

class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_date'
    # 기준이 되는 날짜 필드

class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_date'
    make_object_list = True

class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_date'

class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_date'

class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_date'

class TagTV(TemplateView):
    template_name = 'tagging/tagging_cloud.html'
    # 템플릿 랜더링

class PostTOL(TaggedObjectList):
    model = Post
    template_name = 'tagging/tagging_post_list.html'

class search(TemplateView):
    template_name = 'blog/search.html'