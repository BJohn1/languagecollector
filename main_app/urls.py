from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('languages/', views.languages_index, name='index'),
  path('languages/<int:language_id>/', views.languages_detail, name='detail'),
  path('languages/create/', views.LanguageCreate.as_view(), name='languages_create'),
  path('languages/<int:pk>/update/', views.LanguageUpdate.as_view(), name='languages_update'),
  path('languages/<int:pk>/delete/', views.LanguageDelete.as_view(), name='languages_delete'),
  path('languages/<int:language_id>/add_upskill/', views.add_upskill, name='add_upskill'),
]