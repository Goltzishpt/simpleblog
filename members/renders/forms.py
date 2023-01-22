from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from blog.models import Profile
from django.contrib.auth.forms import ReadOnlyPasswordHashField, AuthenticationForm
from django.utils.translation import gettext_lazy as _


class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'telegram_url', 'facebook_url', 'linkedIn_url', 'instagram_url', 'pinterest_url')
        labels = {'bio': 'Bio', 'profile_pic': 'Photo', 'telegram_url': 'Telegram', 'facebook_url': 'Facebook',
                  'linkedIn_url': 'LinkedIn', 'instagram_url': 'Instagram', 'pinterest_url': 'Pinterest'}
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'formControl', 'placeholder': 'Enter your bio'}),
            'telegram_url': forms.TextInput(attrs={'class': 'formControl', 'placeholder': 'Enter your Telegram'}),
            'facebook_url': forms.TextInput(attrs={'class': 'formControl', 'placeholder': 'Enter your facebook'}),
            'linkedIn_url': forms.TextInput(attrs={'class': 'formControl', 'placeholder': 'Enter your LinkedIn'}),
            'instagram_url': forms.TextInput(attrs={'class': 'formControl', 'placeholder': 'Enter your Instagram'}),
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

