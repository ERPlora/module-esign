from django.urls import path
from . import views

app_name = 'esign'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('documents/', views.documents, name='documents'),
    path('settings/', views.settings, name='settings'),
]
