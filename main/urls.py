from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('conquistas/', views.conquistas_list, name='conquistas'),
    path('conquistas/<slug:slug>/', views.conquista_detail, name='conquista_detail'),
    path('noticias/<slug:slug>/', views.noticia_detail, name='noticia_detail'),
    path('bibliografia/<slug:slug>/', views.bibliografia_detail, name='bibliografia_detail'),
    path('search_ajax/', views.search_ajax, name='search_ajax'),
    path('search/', views.search_results, name='search_results'),
]
