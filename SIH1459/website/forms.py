from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Scheme, Course, College


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
    duration = forms.CharField(required=True,
                                  widget=forms.widgets.TextInput(
                                      attrs={'placeholder': 'Course Duration', 'class': 'form-control'}),
                                  label='')

    class Meta:
        model = Course
        fields = ('code', 'name', 'duration')

class AddCollegeForm(forms.ModelForm):
    name = forms.CharField(required=True,
                           widget=forms.widgets.TextInput(
                               attrs={'placeholder': 'College Name', 'class': 'form-control'}),
                           label='')
    code = forms.CharField(required=True,
                           widget=forms.widgets.TextInput(
                               attrs={'placeholder': 'College Code', 'class': 'form-control'}),
                           label='')
    state = forms.CharField(required=True,
                                  widget=forms.widgets.TextInput(
                                      attrs={'placeholder': 'College state', 'class': 'form-control'}),
                                  label='')

    city = forms.CharField(required=True,
                               widget=forms.widgets.TextInput(
                                   attrs={'placeholder': 'College cty ', 'class': 'form-control'}),
                               label='')

    pincode = forms.CharField(required=True,
                           widget=forms.widgets.TextInput(
                               attrs={'placeholder': 'College pincode', 'class': 'form-control'}),
                           label='')

    address = forms.CharField(required=True,
                           widget=forms.widgets.TextInput(
                               attrs={'placeholder': 'College address', 'class': 'form-control'}),
                           label='')
    phone = forms.CharField(required=True,
                           widget=forms.widgets.TextInput(
                               attrs={'placeholder': 'College phone', 'class': 'form-control'}),
                           label='')

    class Meta:
        model = College
        fields = ('code', 'name', 'state', 'city', 'pincode', 'address', 'phone')
