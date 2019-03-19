from django import forms
from .models import Project, Profile, DesignRating, UsabilityRating, ContentRating


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user', 'profile', 'posted_on']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']


class DesignForm(forms.ModelForm):
    class Meta:
        model = DesignRating
        fields = ['rating']


class UsabilityForm(forms.ModelForm):
    class Meta:
        model = UsabilityRating
        fields = ['rating']


class ContentForm(forms.ModelForm):
    class Meta:
        model = ContentRating
        fields = ['rating']
