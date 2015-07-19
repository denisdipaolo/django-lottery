from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^', views.available_games_list, name='available_games_list'),
]
