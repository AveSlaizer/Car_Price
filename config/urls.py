"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, re_path
from apps.mainpage.views import MainPage
from apps.test_app.views import show_garage, show_account

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPage.show_main_page, name='main'),
    path('garage/', show_garage, name='garage'),
    path('account/', show_account, name='account'),
    re_path(r'\w+', MainPage.show_main_page, name='main'),
]
