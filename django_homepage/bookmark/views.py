# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import DetailView,ListView
from django.shortcuts import render
from bookmark.models import Bookmark
# Create your views here.

class BookmarkLV(ListView):
    model = Bookmark

class BookmarkDV(DetailView):
    model = Bookmark
