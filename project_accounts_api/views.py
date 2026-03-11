from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework import generics,permissions
from rest_framework.response  import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework import status
from django.utils import timezone
# import pdb

# Create your views here.

class RagisterView(APIView):
    template_name = 'rest_framework/api.html'
    def post(self,request,*args, **kwargs):
        try:
            context=request.data
            serializer=UserSerializer(data=request.data)
            # pdb.set_trace()
            if serializer.is_valid():
                user=serializer.save()
                print('ragister done')
                return Response({
                    'status':200,
                    'data':UserSerializer(user).data,
                    'massege':'ragister is successfull'
                })
            print('ragister fail')
            
            return Response({
                'status':403,
                'errors':serializer.errors
             })
            
        except Exception as e:
            print(e)
            return Response({
                'status':404,
                'errors':'somthing went worng'
            })

class LogoutView(APIView):
     permission_classes = (IsAuthenticated,)
     def post(self, request):
          
          try:
               refresh_token = request.data["refresh_token"]
               token = RefreshToken(refresh_token)
               token.blacklist()
               return Response(status=status.HTTP_205_RESET_CONTENT)
          except Exception as e:
               return Response(status=status.HTTP_400_BAD_REQUEST)
          

class HomeView(APIView):
   permission_classes = (IsAuthenticated, )
   def get(self, request):
        content = {'message': 'Welcome to the JWT Authentication page using React Js and Django!'}
        return Response(content)


class UsersData(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

class UserData(APIView):
    permission_classes = (IsAuthenticated, )
    def get(self, request, *args, **kwargs):
        user_id = request.user.id
        data=User.objects.get(id=user_id)
        userdata1=UserSerializer(data)
        return Response(userdata1.data)


class UserViewDU(generics.DestroyAPIView,generics.UpdateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    lookup_field='id'
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EventsView(generics.CreateAPIView,generics.ListAPIView):
    queryset=Eventes.objects.all()
    serializer_class=EventSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class EventsViewDU(generics.DestroyAPIView,generics.UpdateAPIView):
    queryset=Eventes.objects.all()
    serializer_class=EventSerializer
    lookup_field='id'
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    
class GenresView(generics.CreateAPIView,generics.ListAPIView):
    queryset=Genre.objects.all()
    serializer_class=GenreSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class GenreViewDU(generics.DestroyAPIView,generics.UpdateAPIView):
    queryset=Genre.objects.all()
    serializer_class=GenreSerializer
    lookup_field='id'
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class CartView(generics.ListAPIView):
    permission_classes = (IsAuthenticated, )
    queryset=Cart.objects.all()
    serializer_class=CartSerializer
    
class AddCartView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset=Cart.objects.all()
    serializer_class=AddCartSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

class CartViewDU(generics.DestroyAPIView,generics.UpdateAPIView):
    queryset=Cart.objects.all()
    serializer_class=CartSerializer
    lookup_field='id'
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def UserData(request,id):
#     data=User.objects.get(id=id)
#     userdata=UserSerializer(data)
#     print('////////////////////////////////////////////////////////////')
#     print(userdata.data)
#     print('////////////////////////////////////////////////////////////')
#     return Response(userdata.data)


# @api_view(['POST'])
# def RagisterView(request):
#     try:
#         context=request.data
#         print('////////////////////////////////////////////////////////////')
#         print(context)
#         print('////////////////////////////////////////////////////////////')
#         serializer=UserSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response({
#                 'status':403,
#                 'errors':serializer.errors
#             })
#         serializer.save()
#         return Response({
#             'status':200,
#             'data':context,
#             'massege':'ragister is successfull'
#         })
            
#     except Exception as e:
#         print(e)
#         return Response({
#             'status':404,
#             'errors':'somthing went worng'
#         })


