
from django import forms
from django.contrib.auth.models import User


class UserRegistration(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )
        
    def clean_password(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("Password didn't match")

    # def check_password(self):
    #     cd = self.changed_data
    #     if cd('password') != cd('password2'):
    #         raise forms.ValidationError('Incorrect password')