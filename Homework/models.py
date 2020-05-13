from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.forms import NullBooleanSelect


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_teacher = models.BooleanField(default=False, blank=True)
    schoolclass = models.ForeignKey('SchoolClass', on_delete=models.CASCADE, null=True)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, null=True)


class SchoolClass(models.Model):
    name = models.CharField(max_length=56)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=56)

    def __str__(self):
        return self.name


GRADES_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
)


class Homework(models.Model):
    title = models.CharField(max_length=56)
    content = models.CharField(max_length=1000)
    student = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    schoolclass = models.ForeignKey(SchoolClass, on_delete=models.CASCADE, null=True)
    grade = models.CharField(max_length=156, choices=GRADES_CHOICES)
    comment = models.CharField(max_length=200)
    deadline = models.DateField(auto_now_add=False, auto_now=False)

    def __str__(self):
        return self.title


# class Homework(models.Model):
#     title = models.CharField(max_length=56)
#     content = models.CharField(max_length=1000)
#     student = models.ManyToManyField(User)
#     subject = models.ManyToManyField(Subject)
#     schoolclass = models.ManyToManyField(SchoolClass)
#     grade = models.CharField(max_length=156, choices=GRADES_CHOICES)
#     comment = models.CharField(max_length=200)
#     deadline = models.DateField(auto_now_add=False, auto_now=False)
#
#     def __str__(self):
#         return self.title


class Message(models.Model):
    text = models.CharField(max_length=250)
    date_pub = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
