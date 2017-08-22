from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^adduser$', views.adduser),
    url(r'^destroy/(?P<post_id>\d+)$', views.destroy_post),
    url(r'^like/(?P<post_id>\d+)$', views.like),
    url(r'^login$', views.login),
    url(r'^secrets$', views.secrets),
    url(r'^post$', views.post),
    url(r'^back$', views.back),
    url(r'^pop_secrets$', views.pop_secrets),
    url(r'^logout$', views.logout),
]
