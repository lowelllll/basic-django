# -*- coding:UTF-8 -*-
# 커스텀 필드 작성
from django.db.models.fields.files import ImageField , ImageFieldFile
# 장고 기본 필드 임포트
from PIL import Image
# 이미지처리 라이브러리
import os

def _add_thumb(s): # 기존 이미지 파일명 -> 썸네일 이미지 파일명
    parts = s.split(".")
    parts.insert(-1,'thumb')
    if parts[-1].lower() not in ['jpg','jpeg']:
        parts[-1]='jpg' # 확장자가 jpg,jpeg가 아니면 jpg로 바꿈
    return ".".join(parts)
    # ex) abc.jpg -> abc.thumb.jpg

class ThumbnailImageFieldFile(ImageFieldFile): # ImageFieldFile 파일시스템에 직접 파일을 쓰고 지우는 작업
    def _get_thumb_path(self):
        return _add_thumb(self.path)
    thumb_path = property(_get_thumb_path) # 이미지를 처리하는 필드는 url,경로를 제공해야함
                                        # 원본파일의 경로인 path속성에 추가해 썸네일의 경로 thumb_path 속성을 만들어줌

    def _get_thumb_url(self):
        return _add_thumb(self.url)
    thumb_url = property(_get_thumb_url) # 원본파일의 url인 url속성에 추가해 썸네의 URL인 thumb_url 속성을 만들어줌

    def save(self,name,content,save=True): # 파일시스템에 파일을 저장,생성하는 메소드
        super(ThumbnailImageFieldFile,self).save(name,content,save) # 부모클래스(ImageFieldFile)의 메소드(save)를 호출 , 원본 이미지 저장
        img = Image.open(self.path) # 이미지 열기
        size = (128,128)
        img.thumbnail(size,Image.ANTIALIAS) # 썸네일 이미지를 만듬

        background = Image.new('RGBA',size,(0,0,0,1)) # background - img 생성
        background = background.convert("RGB")
        background.paste(
            img,(int((size[0]-img.size[0])/2),int((size[1]-img.size[1])/2) )) # 썸네일 ,백그라운드 이미지 합쳐 썸네일 이미지를 만듬
        background.save(self.thumb_path,'JPEG')
        # 합쳐진 최종 이미지를 JPEG 형식으로 thumb_path에 저장함

    def delete(self,save=True):
        if os.path.exists(self.thumb_path): # 경로가 있으면
            os.remove(self.thumb_path) # 파일을 삭제함
        super(ThumbnailImageFieldFile,self).delete(save)# 썸네일 이미지도 삭제함


class ThumbnailImageField(ImageField): # 장고 모델정의에 사용하는 필드
    attr_class = ThumbnailImageFieldFile # file 처리 클래스를 attr_class 속성에 지정함
    def __init__(self,thumb_width=128,thumb_height=128,*args,**kwargs):
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height
        super(ThumbnailImageField,self).__init__(*args,**kwargs) # 속성초기화


