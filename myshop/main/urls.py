from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shop', views.shop, name='shop'),
    path('contacts', views.contacts, name='contacts'),
    path('about', views.about, name='about'),
    path('add', views.addproduct, name='addproduct'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
