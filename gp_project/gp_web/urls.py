from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('error/', views.error, name="error"),
    path('gallery/', views.gallery, name="gallery"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)