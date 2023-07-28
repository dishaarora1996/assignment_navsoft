from django.shortcuts import render
from rest_framework.exceptions import NotFound
from rest_framework.settings import api_settings
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegistrationSerializer, ProfileSerializer
from rest_framework import status
from .models import Profile
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import parser_classes


# Create your views here.


class CustomAuthToken(ObtainAuthToken):

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                       context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
    

class RegistrationView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    queryset = User.objects.all()

    # def post(self, request):
    #     serializer = RegistrationSerializer(data=request.data)
    #     data ={}
    #     if serializer.is_valid():
    #         account = serializer.save()
    #         data['response'] = 'Registration Successful'
    #         data['username'] = account.username
    #         data['email'] = account.email
    #         token = Token.objects.get(user=account).key
    #         data['token'] = token
    #     else:
    #         data = serializer.errors


    #     return Response(data)
    
class LogoutView(APIView):

    def post(self, request):

        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

   
@parser_classes((MultiPartParser,))
class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

# class ProfileView(APIView):

#     def get(self, request, pk=None):
#         try:
#             profile = Profile.objects.get(id=pk)
#         except Profile.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#         serializer = ProfileSerializer(profile)
#         return Response(serializer.data)


#     def put(self, request, pk=None):
#         try:
#             profile = Profile.objects.get(id=pk)
#         except Profile.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#         serializer = ProfileSerializer(profile, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'response': 'Profile Updated Successfully', 'data': serializer.data}, status=status.HTTP_200_OK)
#         else:
#             return Response({'error': serializer.errors})
        
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
