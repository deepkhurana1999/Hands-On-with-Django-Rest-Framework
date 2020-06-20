from rest_framework import serializers
from .models import Game as Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields ='__all__'
        read_only_fields = ['user']


'''
    def valid_system_requirements(self,value):
        if len(value) > 300:
            raise serializers.ValidationError("This is way too long.")
        return value

    def validate(self, data):
        system_requirements = data.get("content", None)
        if content == "":
            content =None
        image = data.get("image",None)
        if content is None and image is None:
            raise serializers.ValidationError("Requirements or image is required.")
        return data
   
    Use to create custom validation functions
    def valid_<fieldname>(self,value):
        return

        '''