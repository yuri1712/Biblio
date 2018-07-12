from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Livro_list, name='Livro_list'),
]
