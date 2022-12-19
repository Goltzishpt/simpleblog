from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from django.db import models
from theblog.models import Profile
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import gettext_lazy as _


class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'website_url', 'facebook_url', 'twitter_url', 'instagram_url', 'pinterest_url')
        labels = {'bio': 'Bio', 'profile_pic': 'Photo', 'website_url': 'Website', 'facebook_url': 'Facebook',
                  'twitter_url': 'Twitter', 'instagram_url': 'Instagram', 'pinterest_url': 'Pinterest'}

        widgets ={
            'bio': forms.Textarea(attrs={'class': 'formControl', 'placeholder': 'Enter your bio'}),
            'website_url': forms.TextInput(attrs={'class': 'formControl', 'placeholder': 'Enter your website'}),
            'facebook_url': forms.TextInput(attrs={'class': 'formControl', 'placeholder': 'Enter your facebook'}),
            'twitter_url': forms.TextInput(attrs={'class': 'formControl', 'placeholder': 'Enter your twitter'}),
            'instagram_url': forms.TextInput(attrs={'class': 'formControl', 'placeholder': 'Enter your instagram'}),
            'pinterest_url': forms.TextInput(attrs={'class': 'formControl', 'placeholder': 'Enter your pinterest'}),
            'profile_pic': forms.FileInput(attrs={'class': 'formControl'}),
        }


class SignupForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'formControl'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'formControl'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'formControl'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'formControl'
        self.fields['password1'].widget.attrs['class'] = 'formControl'
        self.fields['password2'].widget.attrs['class'] = 'formControl'


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'formControl'}), label='Email')
    first_name = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'formControl'}), label='First name')
    last_name = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'formControl'}), label='Last name')
    username = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'formControl'}), label='Username')
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'formControl', 'type': 'password'}),
                                   label='Old password')
    new_password1 = forms.CharField(max_length=100, label='New password',widget=forms.PasswordInput(
                                    attrs={'class': 'formControl', 'type': 'password'}))
    new_password2 = forms.CharField(max_length=100, label='New password again',  widget=forms.PasswordInput(
                                    attrs={'class': 'formControl', 'type': 'password',}))
    password = ReadOnlyPasswordHashField(label=_(""), help_text=_('',), widget=forms.PasswordInput(
                                    attrs={'class': 'passHidden ', 'type': 'password'}))
    # last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'formControl'}))
    # is_superuser = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    # is_staff = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    # is_active = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    # date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        labels = {'username': '', 'first_name': '', 'last_name': '', 'email': '', 'old_password': '',
                  'new_password1': '', 'new_password2': ''}
        fields = ('username', 'first_name', 'last_name', 'email', 'old_password', 'new_password1', 'new_password2')


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
