from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.portfolio),
    url(r'^projects$', views.projects),
    url(r'^me$', views.me),
    url(r'^testimonials$', views.testimonials)
]
