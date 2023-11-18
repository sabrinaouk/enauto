from django.urls import path
from . import views
from .views import *
 

#vms = routers.DefaultRouter()
#vms.register(r'session/', AuthVMView, basename='session')

urlpatterns = [
    path('create/', views.create_vm, name='session'),
    #path('<int:pk>/', views.ArticleDetailView.as_view(), name='article-detail'),
]
# urlpatterns = [
#      # path('gestionComptesChefService/', include(router.urls)),
#     path('auth/', AuthVMView.as_view()),
#     # path('DeclarationResponsable', DeclarationResponsable.as_view()),
    
#urlpatterns = VMs.urls


