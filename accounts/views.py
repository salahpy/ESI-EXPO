from django.shortcuts import render
from django.http import JsonResponse
from .models import Students, User
import json

def get_students(request):
    if request.method == 'GET':
        user_ids = Students.objects.values_list('user_id', flat=True)
        my_data = User.objects.filter(id__in=user_ids)
        data_list = []
        for item in my_data:
            data_dict = {
                'email': item.email,
                'first_name': item.first_name,
                'last_name': item.last_name,
            }
            data_list.append(data_dict)
        response_data = {'data': data_list}
        return JsonResponse(response_data, safe=False)

