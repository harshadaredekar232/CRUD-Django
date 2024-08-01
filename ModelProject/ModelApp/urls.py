from django.urls import path
from . import views

urlpatterns = [
    path('', views.display, name = 'display'),
    path('create/', views.create, name = 'create'),
    path('createS/', views.create_Staff, name = 'createS'),
    path('edit/<int:sid>', views.edit, name="edit"),
    path('delete/<int:sid>', views.delete, name="delete"),
    path('search_male/',views.search_male, name="search_male"),
    path('search_female/',views.search_female, name="search_female"),

]
