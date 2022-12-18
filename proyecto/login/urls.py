from django.conf import settings
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.decorators import login_required

from . import views

from django.urls import path,include

urlpatterns=[
    
    path('principal/', views.principal, name='principal'),
   
]