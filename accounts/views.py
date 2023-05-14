from django.shortcuts import render
from django.http import JsonResponse
from .models import Students, User
import json
## fatima code using rest framework to reate Projects api for  crud methode 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Projects 
from .serializers import ProjectsSerializer
from rest_framework import serializers, mixins, viewsets, generics
from rest_framework import status
from rest_framework.views import APIView

## fatima code 

def get_students(request):
    if request.method == 'GET':
        user_ids = Students.objects.values_list('user_id', flat=True)
        my_data = User.objects.filter(id__in=user_ids)
        data_list = []
        for item in my_data:
            data_dict = {
                'email': item.email,
                'username': item.username,
                'first_name': item.first_name,
                'last_name': item.last_name,
            }
            data_list.append(data_dict)
        response_data = {'data': data_list}
        return JsonResponse(response_data, safe=False)


#############################################################################################  
# fatima code : rest framework for projecs models 
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_projects': '/',
        'Search by Category': '/?category=category_name',
        #'Search by Subcategory': '/?subcategory=category_name',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }

    return Response(api_urls)


## the creat methode for object 
##############################################################

# @api_view(['POST'])
# def add_Project(request):
#     serializer = ProjectsSerializer(data=request.data)
    
#     if Projects.objects.filter(**request.data).exists():
#         raise serializers.ValidationError('This data already exists')
#     # TODO: create_by ==> id --> object_id , suprivased_by ==> object_id 
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response(status=status.HTTP_400_BAD_REQUEST)
##############################################################




class AddProject(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView,
                  mixins.UpdateModelMixin): 
    serializer_class = ProjectsSerializer
    queryset = Projects.objects.all()
    ## the add   methode for projects
    def post(self, request):
        serializer = ProjectsSerializer(data=request.data)
    
        # if Projects.objects.filter(**request.data).exists():
        #     raise serializers.ValidationError('This data already exists')
      
        if serializer.is_valid():
            created_by_data = request.data.get('created_by', [])
            supervised_by_data = request.data.get('supervised_by', [])
            project = serializer.save(
    
               
            )

            # Add the created_by and supervised_by relationships
            project.created_by.set(created_by_data)
            project.supervised_by.set(supervised_by_data)

            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    ## the update  methode for projects
    def put(self, request,project_id):
            project = Projects.objects.get(id=project_id)
            print(project)
            serializer = ProjectsSerializer(project,data=request.data)
        
            # if Projects.objects.filter(**request.data).exists():
            #     raise serializers.ValidationError('This data already exists')
        
            if serializer.is_valid():
                created_by_data = request.data.get('created_by', [])
                supervised_by_data = request.data.get('supervised_by', [])
                project = serializer.save(
        
                
                )

                # Add the created_by and supervised_by relationships
                project.created_by.set(created_by_data)
                project.supervised_by.set(supervised_by_data)

                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



## the view / listing  methode for projects

   
@api_view(['GET'])
def view_Projects(request):
	
	
    projects = Projects.objects.all()
    serializer = ProjectsSerializer(projects,many=True)
    
    return JsonResponse(serializer.data,safe=False)


## the delete  methode for object
@api_view(['DELETE'])
def delete_project(request,project_id):
    try:
        project = Projects.objects.get(id=project_id)
    except Projects.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    project.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# the update methode for projects model 
