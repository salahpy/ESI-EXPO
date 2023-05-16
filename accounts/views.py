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
from django.db.models import Q


## end fatima code 

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








####### filter by category ###
class CategoryList(generics.ListAPIView):
    serializer_class = ProjectsSerializer

    def get_queryset(self):
        return Projects.objects.filter(category=self.kwargs['category'])
    
    
    
######## filter by multiple parameter ###


## or between multiple parameters version  ###


# class ProjectsViewSet(APIView):
#     def get(self, request):
        
#         category = request.GET.get('category')
#         year = request.GET.get('year')
#         used_techs = request.GET.get('used_techs')
        
#         query = Q(category=category, year=year)
#         if ',' in used_techs:
#             used_techs = used_techs.split(',')            
#             for search_string in used_techs:
#                 query |= Q(used_techs__contains=search_string)
#         else:
#             query |= Q(used_techs__contains=used_techs)
        
#         results = Projects.objects.filter(query)  
#         print(category, year,used_techs)
     
#         serializer = ProjectsSerializer(results,many=True)  
#         return JsonResponse(serializer.data,safe=False)
    


## and  between multiple parameters version  ###
class ProjectsViewSet(APIView):
    def get(self, request):
        category = request.GET.get('category')
        year = request.GET.get('year')
        used_techs = request.GET.get('used_techs')

        query = Q()
        if category:
            query &= Q(category=category)
        if year:
            query &= Q(year=year)
        if used_techs:
            if ',' in used_techs:
                used_techs = used_techs.split(',')
                for search_string in used_techs:
                    query &= Q(used_techs__contains=search_string)
            else:
                query &= Q(used_techs__contains=used_techs)

        results = Projects.objects.filter(query)
        print(category, year, used_techs)

        serializer = ProjectsSerializer(results, many=True)
        return JsonResponse(serializer.data, safe=False)


    
## search function by any field 
# def search_projects(query):
#     fields = ['title', 'description', 'year', 'category', 'used_techs']
#     queries = [Q(**{field + '__icontains': query}) for field in fields]
#     query = Q()
#     for item in queries:
#         query |= item
#     results = Projects.objects.filter(query)
#     return results






# def search_projects(query):
#     fields = ['title', 'description', 'year', 'category', 'used_techs']
#     results = Projects.objects.filter(
#         Q(created_by__name__icontains=query) |
#         Q(supervised_by__name__icontains=query)
#     )
#     for field in fields:
#         results |= Projects.objects.filter(**{field + '__icontains': query})
#     return results

## or between multiple parameters version  ###

class Search(APIView):
    def get(self, request):
        title = request.GET.get('title')
        category = request.GET.get('category')
        year = request.GET.get('year')
        used_techs = request.GET.get('used_techs')
        
        query = Q(category=category, year=year,title=title)
        if ',' in used_techs:
            used_techs = used_techs.split(',')            
            for search_string in used_techs:
                query |= Q(used_techs__contains=search_string)
        else:
            query |= Q(used_techs__contains=used_techs)
        
        results = Projects.objects.filter(query)  
        print(title,category, year,used_techs)
     
        serializer = ProjectsSerializer(results,many=True)  
        return JsonResponse(serializer.data,safe=False)
    


       
          
        
