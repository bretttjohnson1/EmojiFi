from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('emojifi', views.emojifi, name='emojifi'),
    path('emojifi_types', views.emojifi_types, name='emojifi_types'),
]
