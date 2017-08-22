from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^adduser$', views.adduser, name = 'add'),
    url(r'^delete$', views.delete, name = 'del'),
    url(r'^success$', views.success, name = 'suc')
]
