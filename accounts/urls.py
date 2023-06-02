from django.urls import path
from . import views
urlpatterns = [
    path('UsersList/', views.get_students, name='get_students'),
    path('send-email/<str:email1>/<str:email2>/', views.send_email, name='send_email'),
    path('ProjectList/', views.ApiOverview, name='ApiOverview'),
    path('MyProjectList/<int:user_id>/', views.get_projects_by_user, name='get_projects_by_user'),
    path('ProjectList/create/', views.AddProject.as_view(), name='add-items'),
    path('ProjectList/all/', views.view_Projects, name='view_items'),
    path('ProjectList/delete/<int:project_id>/', views.delete_project, name='delete-project'),
    path('ProjectList/update/<int:project_id>/', views.AddProject.as_view(), name='update-items'),  
    path('ProjectList/category/<str:category>/',views.CategoryList.as_view(), name='projects-list-filtered'),
    path('ProjectList/filter/',views.ProjectsViewSet.as_view(), name='filtring'),
    #regex = path(r'ProejctList/filter/(?P<category>Web-app|App|Arduino|Desktop App)/?(?P<year>[2-5]{1})/$', views.ProjectsViewSet.as_view(), name='filtring')
    #path('ProjectList/search/',views.search_projects, name='searching')
]