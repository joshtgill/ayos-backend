from django.urls import path
from . import views

urlpatterns = [
    path('<path:path>/', views.generate, name='generate')
]
