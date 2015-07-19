from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.partecipation, name='partecipation'),
    url(r'(?P<game_id>[0-9]+)/$', views.partecipation, name='partecipation'),
    url(r'confirmation/$', views.confirmation, name='confirmation'),
]
