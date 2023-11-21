from django.urls import path
from . import views
from .views import *
 



urlpatterns = [
    path('create/', views.create_vm, name='session'),
    path('getvm/<uuid:pk>/', views.get_Onevm, name='details'),
    # path('deletevm/<uuid:pk>/', views.delete_Onevm, name='delte'),
    ]




