# from django.conf.urls import url
# from django.urls import path
# from . import views
#
# urlpatterns = [
#     url(r'^hello$', views.hello),#url() is not useful
#     path('', views.hello),
#     path('runoob/', views.runoob),
# ]

from django.urls import path
from django.conf.urls import url
from . import views, testdb,search,search2,main
urlpatterns = [
    path('',main.jumppage),
    path('runoob/', views.runoob),
    url(r'^search-form/$', search.search_form),
    url(r'^search/$', search.search),
    url(r'^search-post/$', search2.search_post),
    url(r'^search-post-back/$', search2.search_post_back),
]

