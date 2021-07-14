
# -*- coding: utf-8 -*-
from . import testdb

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators import csrf
 
# 接收POST请求数据

def search_post(request):
    return render(request, "post.html")

def search_post_back(request):
    if request.POST.get('submit')=='添加数据':
        return testdb.add(request)
    elif request.POST.get('submit')=='删除数据':
        return testdb.delete(request)
    elif request.POST.get('submit')=='显示所有数据':
        return testdb.show_all(request)
    else:
        return testdb.change(request)
