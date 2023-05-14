from django.urls import path
from . import views

urlpatterns = [
    path('StudentsList/', views.get_students, name='get_students'),
    path('ProejctList/', views.ApiOverview, name='ApiOverview'),
    path('ProejctList/create/', views.AddProject.as_view(), name='add-items'),
    path('ProejctList/all/', views.view_Projects, name='view_items'),
    path('ProejctList/<int:project_id>/', views.delete_project, name='delete-project'),
     
 
]