from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User
from rest_framework import filters 
from django.db.models import Q

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()
    
    def get_queryset(self):

        serializer_class = UserSerializer
        queryset = User.objects.all()

        name = self.request.query_params.get('name')

        if name:

            queryset = User.objects.all().filter(Q(first_name=name) | Q(last_name=name))

        return queryset