from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),

    #path('', views.post_list, name='post_list'),
    #path('character/<str:pk>/', views.character_detail, name='character_detail'),
    #path('equipement/<str:pk>/', views.equipement_detail, name='equipement_detail'),
    
    #path('character/<str:id_character>/', views.post_list, name='character_detail'),
    #path('character/<str:id_character>/?<str:message>', views.character_detail, name='character_detail_mes'),
    #path('test-form/', views.character_detail, name='test_form'),


]