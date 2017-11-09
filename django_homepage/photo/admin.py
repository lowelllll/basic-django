# -*- coding: UTF-8 -*-
from django.contrib import admin
from photo.models import Album,Photo
# Register your models here.

class PhotoInline(admin.StackedInline):
    # 외래키로 연결된 Album,Photo는 1:N 관계 성
    # 앨범 객체를 보여줄때 photo객체도 보여줌
    # Stackedinline 세로
    # Tabularinline 테이블 모양
    model = Photo
    # 추가로 보여주는 테이블
    extra = 2
    # 추가로 입력할 수 있는 포토테이블 객체 2개

class AlbumAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
    # Photoinline 클래스에서 정의한 사항을 같이 보여줌
    list_display = ('name','description')

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title','upload_date')

admin.site.register(Album,AlbumAdmin)
admin.site.register(Photo,PhotoAdmin)
