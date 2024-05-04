"""
URL configuration for project8 project.

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
from django.urls import path
from modelsapp.views import HomeView,InsertInput,InsertView,DisplayView,DeleteInput,DeleteView,UpdateInputView,UpdateView

urlpatterns = [

    path('admin/', admin.site.urls),
    path('lokeshit',HomeView.as_view()),
    path('modelsapp/insertinput/',InsertInput.as_view()),
    path('modelsapp/insertinput/insert/',InsertView.as_view()),
    path('modelsapp/display/',DisplayView.as_view()),
    path('modelsapp/deleteinput/',DeleteInput.as_view()),
    path('modelsapp/deleteinput/delete/',DeleteView.as_view()),
    path('modelsapp/updateinput/',UpdateInputView.as_view()),
    path('modelsapp/updateinput/update/',UpdateView.as_view()),
]
