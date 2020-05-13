from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from django.forms import ModelForm

from Homework.models import SchoolClass, Profile, Subject, Homework


def password_validation(value):
    if len(value) < 8:
        raise ValidationError("haslo za krotke min 8 znakow")


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput, validators=[password_validation])
    re_password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    is_teacher = forms.BooleanField(required=False)
    schoolclass = forms.ModelChoiceField(queryset=SchoolClass.objects.all(), required=False)
    subject = forms.ModelChoiceField(queryset=Subject.objects.all(), required=False)

    def clean(self):
        cleaned_data = super().clean()
        if not self.errors:
            if cleaned_data['password'] != cleaned_data['re_password']:
                raise ValidationError("hasla nie sie identyczne")
        return self.cleaned_data


GRADES_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
)


class DateInput(forms.DateInput):
    input_type = 'date'


class HomeworkForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()
    student = forms.ModelChoiceField(queryset=User.objects.all(), required=False)
    subject = forms.ModelChoiceField(queryset=Subject.objects.all(), required=False)
    schoolclass = forms.ModelChoiceField(queryset=SchoolClass.objects.all(), required=False)
    grade = forms.ChoiceField(choices=GRADES_CHOICES, required=False)
    comment = forms.CharField(required=False)
    deadline = forms.DateField(widget=DateInput)

#
# class HomeworkForm(ModelForm):
#     student = forms.ModelChoiceField(queryset=User.objects.all())
#     subject = forms.ModelChoiceField(queryset=Subject.objects.all())
#     schoolclas = forms.ModelChoiceField(queryset=SchoolClass.objects.all())
#
#     class Meta:
#         model = Homework
#         fields = ['title', 'content', 'student', 'subject', 'schoolclass', 'deadline']
