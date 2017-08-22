from django.conf.urls import url
from django.contrib import admin
from . import views
from views import Post

urlpatterns = [
    url(r'^$', views.index),
    url(r'^post$', views.post)
]
