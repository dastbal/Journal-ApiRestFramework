# from django.shortcuts import render
from  rest_framework.views import APIView
from  rest_framework.response import Response
from  rest_framework import status ,viewsets , filters
from  rest_framework.authentication import TokenAuthentication
from  rest_framework.authtoken.views import ObtainAuthToken
from  rest_framework.settings import api_settings 
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from  profiles_api import serializers  , models , permissions

class HelloApiView(APIView):
    serializer_class =serializers.HelloSerializer

    def get(self,request,format=None): 
        """ return a list
        """
        an_apiview = [
            'a',
            'b',
            'c',
        ]
        return  Response({'message':'Hello World', 'an_apiview':an_apiview})


    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            apellido = serializer.validated_data.get('apellido')
            messeage = f'Hello {name} {apellido}'
            return Response({'messeage': messeage})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    def put(self,request ,pk=None):
        return Response({'method':'PUT'})
    def patch(self,request ,pk=None):
        return Response({'method':'PATCH'})
    def delete(self,request ,pk=None):
        return Response({'method':'Deleted'})
        

class HelloViewSet(viewsets.ViewSet):
    serializer_class =serializers.HelloSerializer
    def list(self,request):
        a_viewset= [
            'list',
            'create',
            'retrive',
            'update',
            'delete',
            'partial update'
        ]
        return  Response({'message':'HelloWorld', 'a_viewset': a_viewset})
    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            apellido = serializer.validated_data.get('apellido')
            messeage = f'Hello {name} {apellido}'
            return Response({'messeage': messeage})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    def retrieve(self,request, pk=None):
        return Response({'http_method':'GET'})

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer

    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)
class UserLoginApiView(ObtainAuthToken):
    """ Create tokens of authentification"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
class ProfileJournalItemViewSet(viewsets.ModelViewSet):
    authentication_classes =(TokenAuthentication,)
    serializer_class = serializers.ProfileJournalItemSerializer
    queryset = models.ProfileJournalItem.objects.all()




















    # permission_classes =(
    #     permissions.UpdateOwnJournal,
    #     IsAuthenticatedOrReadOnly
    # )


    # def perform_create(self, serializer):
    #     serializer.save(user_profile=self.request.user)

