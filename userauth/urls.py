
from django.urls import include, path
from userauth import views


urlpatterns = [
       path('register/',views.register,name='register'),
       path('signin/',views.signin,name='signin'),
       path('signout/',views.signout,name='signout'),
       path('profile/',views.profile,name='profile'),
       
       

    
] 
