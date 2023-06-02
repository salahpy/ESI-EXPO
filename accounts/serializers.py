from rest_framework import serializers
from .models import User , Projects
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
 
class UserrSerializer(serializers.ModelSerializer):
    role = serializers.CharField()

    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "email", "role", "username", "password", "skills")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User(
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            username=validated_data.get('username', None),
            role=validated_data["role"],
            skills=validated_data.get('skills', None),
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


User = get_user_model()


class UserCreateSerializer(UserCreateSerializer):
    role = serializers.CharField()

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ("id", "email", "first_name", "last_name", "username", "role", "password", "skills")
        



class ProjectsSerializer(serializers.ModelSerializer):
   
    class Meta:
       model = Projects 
       fields = ('title', 'description', 'year', 'category','used_techs','created_by','supervised_by','logo','image','created_at')

        
        
        
        


    