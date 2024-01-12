
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import SiteInfo

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Entrez une adresse email valide.')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class SiteInfoForm(forms.ModelForm):
    class Meta:
        model = SiteInfo
        fields = ['site_name', 'site_url', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }