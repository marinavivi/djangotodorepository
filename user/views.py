from django.shortcuts import render
from .serializers import UserSerializer
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

# Create your views here.

class HomeView(APIView):

    def get(self, request, *args, **kwargs):

        return Response('Home Page')
    

class UserListAPI(generics.ListAPIView):

    model = User

    serializer_class = UserSerializer

    queryset = User.objects.all()


from django.views.generic import DetailView

class UserRetrieveView(DetailView):

    template_name = 'details.html'

    model = User
    serializer_class = UserSerializer

    context_object_name = 'user'

    def detail(request, user_id):
        try:
            user = User.objects.get(pk=user_id)

        except User.DoesNotExist:
            raise Http404("User does not exist")
            
        return render(request, 'details.html', {'user': user})

