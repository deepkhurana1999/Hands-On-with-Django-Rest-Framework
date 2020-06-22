import json

from django.views.generic import View

from rest_framework.authentication import SessionAuthentication
from rest_framework import generics, mixins, permissions
from rest_framework.views import APIView

from API.models import Game as Status
from API.serializers import TaskSerializer as StatusSerializer


# Create your views here.

def is_json(json_data):
    try:
        real_json = json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid

class StatusDetailAPIView(
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    generics.RetrieveAPIView
    ):
    #permission_classes = []
    #authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    #lookup_field = 'id'

    def put(self,request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self,request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    def patch(self,request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    '''
    def perform_update(self, serializer):
        serializer.save(updated_by_user=self.request.user)
    
    def perform_destroy(self,instance):
        if instance is not None:
            return instance.delete()
        return None
    '''

class StatusAPIView(
    mixins.CreateModelMixin, 
    generics.ListAPIView
    ):
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    #authentication_classes = [SessionAuthentication]
    serializer_class  = StatusSerializer
    passed_id = None
    
    def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)
