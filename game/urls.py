from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<game_title>[\w]+)/$', views.game, name='game')
]

