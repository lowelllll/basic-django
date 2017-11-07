# -*- coding:UTF-8 -*-
from __future__ import unicode_literals
from django.db import models

from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse
from tagging.fields import TagField

# Create your models here.

@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField('TITLE',max_length=50)
    slug = models.SlugField('SLUG',unique=True,allow_unicode=True)
    # allow_unicode 한글처리 가능
    description = models.CharField('DESCRIPTOION',max_length=100,blank=True)
    content = models.TextField('CONTENT')
    create_date = models.DateTimeField('Create Date',auto_now_add=True)
    # 날짜와 시간 auto_now_add 객체를 생성할때 시각을 기록
    modify_date = models.DateTimeField('Modify Date',auto_now=True)
    # auot_now 객체가 데이터베이스에 저장될때 시각을 기록
    tag = TagField()

    class Meta: # 필드속성외 다른 속성이 필요할때
        verbose_name = 'post'
        # 테이블의 단수별칭
        verbose_name_plural = 'posts'
        # 테이블의 복수별칭
        db_table = 'my_post'
        # 데이터베이스에 저장되는 테이블 이름 defalut blog_post
        ordering = ('-modify_date',)
        # 객체 리스트 출력시 modify_date 기준으로 내림차순 정렬

    def __str__(self):
        return self.title
    # 객체를 문자열로 표시하기위해
    def get_absolute_url(self):
        return reverse('blog:post_detail',args=(self.slug,))
        # url 패턴을 만들어줌

    def get_previous_post(self):
        return self.get_previous_by_modify_date()
        # modify_date 칼럼 기준으로 이전 포스트를 반환
    def get_next_post(self):
        return self.get_next_by_modify_date()


