from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


from django.views import View
from django.views.generic import UpdateView, FormView

from Homework.forms import LoginForm, RegistrationForm, HomeworkForm
from Homework.models import SchoolClass, Profile, Subject, Homework


def index(request):
    return render(request, 'base.html')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            print('nie udalo sie zalogowac')
        return redirect('/')


class RegistrationView(View):

    def get(self, request):
        form = RegistrationForm()
        return render(request, 'registration.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User()
            user.username = form.cleaned_data['username']
            user.set_password(form.cleaned_data['password'])
            user.email = form.cleaned_data['email']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            profile = Profile(is_teacher=form.cleaned_data['is_teacher'])
            profile.user = user
            profile.schoolclass = form.cleaned_data['schoolclass']
            profile.subject = form.cleaned_data['subject']
            profile.save()

            return redirect('/')
        return render(request, 'registration.html', {'form': form})


class SchoolClassView(LoginRequiredMixin, View):

    def get(self, request):
        schoolclasses = SchoolClass.objects.all
        return render(request, "schoolclass.html", {'schoolclasses': schoolclasses})


class SchoolClassIdView(LoginRequiredMixin, View):

    def get(self, request, id):
        schoolclass = SchoolClass.objects.get(pk=id)
        profiles = Profile.objects.filter(schoolclass=schoolclass, is_teacher=False)
        return render(request, "schoolclassbyid.html", {"profiles": profiles})


class SubjectsView(LoginRequiredMixin, View):

    def get(self, request):
        subjects = Subject.objects.all
        return render(request, "subjects.html", {"subjects": subjects})


class AddHomeworkView(LoginRequiredMixin, View):
    def get(self, request):
        form = HomeworkForm()
        return render(request, 'addhomework.html', {'form': form})

    def post(self, request):
        form = HomeworkForm(request.POST)
        if form.is_valid():
            homework = Homework()
            homework.title = form.cleaned_data['title']
            homework.content = form.cleaned_data['content']
            homework.student = form.cleaned_data['student']
            homework.subject = form.cleaned_data['subject']
            homework.schoolclass = form.cleaned_data['schoolclass']
            homework.comment = form.cleaned_data['comment']
            homework.deadline = form.cleaned_data['deadline']
            homework.save()


            return redirect('/')
        return render(request, 'addhomework.html', {'form': form})

# class AddHomeworkView(FormView):
#     template_name = 'addhomework.html'
#     form_class = HomeworkForm
#     success_url = '/'
#
#     def form_valid(self, form):
#         title = form.cleaned_data('title')
#         content = form.cleaned_data('content')
#
#         users = User.objects.filter()

class StudentIdView(View):
    def get(self, request, id):
        user = User.objects.get(pk=id)
        homework = Homework.objects.filter(student=user)
        return render(request, 'studentid.html', {'homework': homework})


class UpdateHomework(UpdateView):
    model = Homework
    fields = ['title', 'content', 'grade', 'comment','deadline']
    template_name = 'update_homework.html'
    success_url = '/'


class HomeworkStudentView(View):
    def get(self, request, id):
        subject = Subject.objects.get(pk=id)
        homework = Homework.objects.filter(subject=subject)
        return render(request, 'homeworkstudentview.html', {'homework': homework})


class Test(View):

    def get(self, request):
        return render(request, 'Test.html')
