from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from chatapi.serializers import UserSerializer, GroupSerializer, lBotSerializer
from chatapi.models import lBot

def index(request):
	return HttpResponse('Chatapi Index')


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class lBotList(generics.ListCreateAPIView):
    queryset = lBot.objects.all()
    serializer_class = lBotSerializer

class lBotDetail(generics.RetrieveAPIView):
    queryset = lBot.objects.all()
    serialzer_class = lBotSerializer


#def