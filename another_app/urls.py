from django.urls import path
from . import views

urlpatterns = [
    path('some_models/', views.some_model_list, name='some_model_list'),
    path('some_models/<int:model_id>/', views.some_model_detail, name='some_model_detail'),
]
