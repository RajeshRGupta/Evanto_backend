from django.urls import path
from .views import *

urlpatterns = [
    path('ragister/' , RagisterView.as_view(),name='register'),
    path('logout/', LogoutView.as_view(), name ='logout'),
    path('home/', HomeView.as_view(), name ='home'),
    path('usersdata/', UsersData.as_view(), name ='usersdata'),
    path('userdata/', UserData.as_view(), name ='userdata'),
    path('userdatas/<id>', UserViewDU.as_view(), name ='userdata'),
    path('events/', EventsView.as_view(), name ='events'),
    path('event/<id>', EventsViewDU.as_view(), name ='event'),
    path('genres/', GenresView.as_view(), name ='genres'),
    path('genre/<id>', GenreViewDU.as_view(), name ='genre'),
    path('carts/', CartView.as_view(), name ='carts'),
    path('addcarts/', AddCartView.as_view(), name ='addcarts'),
    path('cart/<id>', CartViewDU.as_view(), name ='cart')

]
