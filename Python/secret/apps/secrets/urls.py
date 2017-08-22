from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^adduser$', views.register, name = 'add'),
    url(r'^success$', views.success, name = 'suc'),
    url(r'^postsecret$', views.POSTsecret, name = 'postSEC'),
    url(r'^(?P<id>\d+)$', views.like),
    url(r'^popular$', views.popular),
    # DELETE #
    url(r'^delete$', views.delete, name = 'del'),
    url(r'^deletePOS$', views.deletePOST)
]
