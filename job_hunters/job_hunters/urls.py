"""
URL configuration for job_hunters project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from pages.views import index

from . import views

urlpatterns = [
    path('', index, name="home"),
    path('admin/', admin.site.urls),
    path('jobs/', include('jobs.urls')),
    path('signup/', include('signup.urls')),
    path('login/', include('login.urls')),
    path('accounts/', include('accounts.urls')),
    path('companies/', include('companies.urls')),
    path('profiles/', include('profiles.urls')),
    path("get_pic/<int:user_id>", views.get_pic, name="get_pic")
]