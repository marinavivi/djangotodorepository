from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse

# Create your views here.

class HomeView(APIView):

    def get(self, request, *args, **kwargs):

        return HttpResponse('<h2>Home Page<h2>')



