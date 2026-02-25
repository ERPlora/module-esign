from django.urls import path
from . import views

app_name = 'esign'

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # Navigation tab aliases
    path('documents/', views.signature_requests_list, name='documents'),


    # SignatureRequest
    path('signature_requests/', views.signature_requests_list, name='signature_requests_list'),
    path('signature_requests/add/', views.signature_request_add, name='signature_request_add'),
    path('signature_requests/<uuid:pk>/edit/', views.signature_request_edit, name='signature_request_edit'),
    path('signature_requests/<uuid:pk>/delete/', views.signature_request_delete, name='signature_request_delete'),
    path('signature_requests/bulk/', views.signature_requests_bulk_action, name='signature_requests_bulk_action'),

    # Settings
    path('settings/', views.settings_view, name='settings'),
]
