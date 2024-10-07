from django.urls import path
from realestateapp import views
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home, name="home"),
    path('mobileViviendas/', views.mobileViviendas, name='mobileViviendas'),
    path('mobileEdificios/', views.mobileEdificios, name='mobileEdificios'),
    path('mobileIndustrias/', views.mobileIndustrias, name='mobileIndustrias'),
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)