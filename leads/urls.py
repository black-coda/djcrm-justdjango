from django.urls import path
from . import views

urlpatterns = [
    path('', views.lead_list, name='home'),
    path('create/', views.lead_create, name='lead_create'),
    path('<int:pk>/', views.lead_details, name='lead_detail',)
]