from django import forms
from django.contrib.auth.forms import UserChangeForm
from.models import post
from.models import edit_profile

class edit_profile_form (forms.ModelForm):
    photo=forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control'}))

    class Meta:
        model = edit_profile
        fields = ('photo',)