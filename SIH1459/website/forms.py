from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Scheme,Course


class AddSchemeForm(forms.ModelForm):
    id = forms.CharField(required=True,
                         widget=forms.widgets.TextInput(attrs={'placeholder': 'Scheme ID', 'class': 'form-control'}),
                         label='')
    name = forms.CharField(required=True,
                           widget=forms.widgets.TextInput(
                               attrs={'placeholder': 'Scheme Name', 'class': 'form-control'}),
                           label='')

    class Meta:
        model = Scheme
        fields = ('id', 'name')


class AddCourseForm(forms.ModelForm):
    code = forms.CharField(required=True,
                           widget=forms.widgets.TextInput(
                               attrs={'placeholder': 'Course Code', 'class': 'form-control'}),
                           label='')
    name = forms.CharField(required=True,
                           widget=forms.widgets.TextInput(
                               attrs={'placeholder': 'Course Name', 'class': 'form-control'}),
                           label='')
    duration = forms.IntegerField(required=True,
                                  widget=forms.widgets.TextInput(
                                      attrs={'placeholder': 'Course Duration', 'class': 'form-control'}),
                                  label='')

    class Meta:
        model = Course
        fields = ('code', 'name', 'duration')
