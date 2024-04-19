
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('dashboard/', views.display_combined_data, name = 'dashboard'),
    #path('answers/', views.display_answers, name='Answer'),
    #path('notes/', views.display_notes, name ='Notes'),
    path('create/', views.add_questions, name = 'Create question'),
]