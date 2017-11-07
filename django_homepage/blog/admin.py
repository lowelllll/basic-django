# -*- coding:UTF-8 -*-
from django.contrib import admin
from blog.models import Post
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','modify_date')
    # Post 객체를 보여줄때 title과 modify_date를 화면에 출력지정
    list_filter = ('modify_date',)
    # 필터사이드바
    search_fields = ('title','content')
    # 검색박스
    prepopulated_fields = {'slug':('title',)}
    # 슬러그는 타이틀에의해 자동으로 채워짐

admin.site.register(Post,BlogAdmin)
