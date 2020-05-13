"""HomeworkApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from Homework import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index),
    path("login/", views.LoginView.as_view()),
    path("registration/", views.RegistrationView.as_view()),
    path("test/", views.Test.as_view()),
    path("schoolclass/", views.SchoolClassView.as_view()),
    path("logout/", views.LogoutView.as_view()),
    path("schoolclass/<int:id>/", views.SchoolClassIdView.as_view()),
    path("subjects/", views.SubjectsView.as_view()),
    path("addhomework/", views.AddHomeworkView.as_view()),
    path("student/<int:id>", views.StudentIdView.as_view()),
    path("homework/<int:pk>", views.UpdateHomework.as_view()),
    path("subjects/<int:id>", views.HomeworkStudentView.as_view()),
]
