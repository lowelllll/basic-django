from django.conf.urls import url
from .views import BookmarkDV,BookmarkLV
urlpatterns = [
    url(r'^$',BookmarkLV.as_view(),name='list'),
    url(r'^(?P<pk>\d+)/$',BookmarkDV.as_view(),name='detail')
]