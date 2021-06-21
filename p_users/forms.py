from django import forms
from django.contrib.auth.models import User

class PatientModelForm (forms.ModelForm):
    password = forms.CharField(max_length=64, widget=forms.PasswordInput)
    #password2 = forms.CharField(max_length=64, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']






