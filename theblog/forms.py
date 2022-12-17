from django import forms
from .models import Post, Category, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body', 'snippet', 'header_image')
        labels = {'title': '', 'title_tag': '', 'author': '', 'category': 'Select category', 'body': '', 'snippet': '', 'header_image': ''}

        widgets = {
            'title': forms.TextInput(attrs={'class': 'formControl', 'placeholder': 'Enter title'}),
            'title_tag': forms.TextInput(attrs={'class': 'formControl', 'placeholder': 'Enter title tag'}),
            'author': forms.TextInput(attrs={'class': 'formControl', 'value': '', 'id': 'elder', 'type': 'hidden'}),
            'category': forms.Select(attrs={'class': 'formControl', 'placeholder': 'Select'}),
            'body': forms.Textarea(attrs={'class': 'formControl', 'placeholder': 'Enter your text'}),
            'snippet': forms.Textarea(attrs={'class': 'formControl', 'value': 'Click Link Above To Read Blog Post...'}),
            'header_image': forms.FileInput(attrs={'class': 'formControl'})

        }

        def __init__(self, *args, **kwargs):
            super(PostForm, self).__init__(*args, **kwargs)
            self.fields['category'] = forms.ModelChoiceField(
                queryset=Category.objects.all(),
                widget=forms.Select(attrs={'class': 'form-control'})
            )


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body', 'snippet')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is Title Placeholder Stuff'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is Title Placeholder Stuff'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
         }
