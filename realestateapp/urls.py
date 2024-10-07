from django.urls import path
from realestateapp import views
from django.conf import settings 
from django.conf.urls.static import static


from .views import test_gcs_access  # Asegúrate de importar la función

urlpatterns = [
    path('',views.home, name="home"),
    path('mobileViviendas/', views.mobileViviendas, name='mobileViviendas'),
    path('mobileEdificios/', views.mobileEdificios, name='mobileEdificios'),
    path('mobileIndustrias/', views.mobileIndustrias, name='mobileIndustrias'),
    path('test-gcs/', test_gcs_access, name='test_gcs'),
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)