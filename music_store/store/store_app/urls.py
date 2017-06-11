from django.conf.urls import url
import store_app
from . import views

urlpatterns = [
    url(r'^$', views.album_list, name='home'),
    url(r'^album_list/$', views.album_list, name='album_list'),
    url(r'^album/(?P<album_id>\d+)$', views.album, name='album'),
    url(r'^basket/$', views.basket, name='basket'),
    url(r'^orders/$', views.orders, name='orders'),
]