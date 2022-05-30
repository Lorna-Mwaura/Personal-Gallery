from django.urls import re_path
from . import views

urlpatterns = [
    re_path('^$', views.welcome),
    re_path('search', views.search_results, name='search_results')
]