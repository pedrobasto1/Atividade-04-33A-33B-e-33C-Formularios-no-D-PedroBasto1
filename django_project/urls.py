"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appdopedro import views

urlpatterns = [
    path('users/login/', views.login_user, name="login"),
    path('users/logout/', views.logout_user, name="logout"),
    path('users', views.create_user),
    path('',views.home, name="home"),
    path('lugares',views.create_lugar),
    path('lugares/update/<id>', views.update_lugar),
    path('lugares/delete/<id>', views.delete_lugar),
    path('kennedy',views.create_kennedy),
    path('kennedy/update/<id1>', views.update_kennedy),
    path('kennedy/delete/<id1>', views.delete_kennedy),
    path('admin/', admin.site.urls),
]
