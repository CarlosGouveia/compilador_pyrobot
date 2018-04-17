from django.conf.urls import url
from core import views


urlpatterns = [
    url(r'^$', views.home, name='home'),

    url(r'^cpf/$', views.homecpf, name='cpfview'),
    url(r'^pos/$', views.homepos, name='posview'),

    url(r'^homecpf/$', views.validacpf, name='cpf'),
    url(r'^homepos/$', views.gerarposfixa, name='pos'),

    url(r'^compilador/$', views.homecompilador, name='compiladorview'),
    url(r'^homecompilador/$', views.compilar, name='compilador'),
]