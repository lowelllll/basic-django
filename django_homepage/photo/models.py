# -*- coding:UTF-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse

from photo.fields import ThumbnailImageField
# 커스텀 필드

# Create your models here.

@python_2_unicode_compatible
class Album(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField('One Line Description', max_length=100, blank=True)

    class Meta:
        # 필드 속성외 다른 속성이 필요할때
            ordering = ['name']
        # 객체리스트를 출력할때 name 으로 오름차순
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('photo:album_detail',args=(self.id,))


@python_2_unicode_compatible
class Photo(models.Model):
    album = models.ForeignKey(Album)
    # 왜래키 사진이 소속된 앨범 객체를 가르키는 reference 역할
    # select 형태로 나타남
    title = models.CharField(max_length=50)
    image = ThumbnailImageField(upload_to='photo/%Y/%m')
    # update_to 저장할 위치
    description = models.TextField('Photo Description', blank=True)
    upload_date = models.DateTimeField('Upload date',auto_now_add=True)

    class Meta:
        ordering = ['title']
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('photo:photo_detail',args=(self.id,))


