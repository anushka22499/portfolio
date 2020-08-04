from django.urls import path
from . import views

# SET THE NAMESPACE!
app_name = 'app_site'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    path('index/',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
]
