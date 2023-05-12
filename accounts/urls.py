from django.urls import path
from . import views

urlpatterns = [
    path('StudentsList/', views.get_students, name='get_students'),
]