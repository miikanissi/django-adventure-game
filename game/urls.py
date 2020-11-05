from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # url(r'^(?P<game_title>[\w]+)/$', views.game, name='game')
    path('game/<slug:slug>/', views.game, name='game')
]

