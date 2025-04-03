from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_image, name='upload'),
    path('result/<int:image_id>/', views.result, name='result'),
]
