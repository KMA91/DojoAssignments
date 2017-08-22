from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name ="index"),
    url(r'^register$', views.register, name = "register"),
    url(r'^success$', views.success, name = "success"),
    url(r'^login$', views.login, name = "login"),
    url(r'^logout$', views.logout, name = "logout"),
    url(r'^postsecret$', views.postsecret, name = "postsecret"),
    url(r'^likesecret/(?P<id>\d+)?$', views.likesecret, name = "likesecret"),
    url(r'^deletesecret/(?P<id>\d+)?$', views.deletesecret, name = "deletesecret"),
    url(r'^popularsecret$', views.popularsecret, name = "popularsecret")
]
