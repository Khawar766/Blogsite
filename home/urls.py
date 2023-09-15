from django.urls import path,include
from .views import homepage,contactus,aboutus,searchbox,handlesignup,handlelogin,handlelogout
urlpatterns = [
    path('',homepage,name='Home'),
    path('contact/',contactus,name='ContactUs'),
    path('about/',aboutus,name='AboutUs'),
    path('search/',searchbox,name='Searchbox'),
    path('signup/',handlesignup,name='HandleSignup'),
    path('login/',handlelogin,name='HandleLogin'),
    path('oauth/',include('social_django.urls',namespace='social')),
    path('logout/',handlelogout,name='HandleLogout'),
    
]
