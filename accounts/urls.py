from django.urls import path
from . import views
urlpatterns = [
    path('StudentsList/', views.get_students, name='get_students'),
    path('ProejctList/', views.ApiOverview, name='ApiOverview'),
    path('ProejctList/create/', views.AddProject.as_view(), name='add-items'),
    path('ProejctList/all/', views.view_Projects, name='view_items'),
    path('ProejctList/delete/<int:project_id>/', views.delete_project, name='delete-project'),
    path('ProejctList/update/<int:project_id>/', views.AddProject.as_view(), name='update-items'),  
    path('ProejctList/category/<str:category>/',views.CategoryList.as_view(), name='projects-list-filtered'),
    path('ProejctList/filter/',views.ProjectsViewSet.as_view(), name='filtring'),
    #regex = path(r'ProejctList/filter/(?P<category>Web-app|App|Arduino|Desktop App)/?(?P<year>[2-5]{1})/$', views.ProjectsViewSet.as_view(), name='filtring')
    
]