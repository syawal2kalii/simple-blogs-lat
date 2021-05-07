from django import forms
from .models import article
from django.forms import ModelForm


class UserForm(forms.Form):
    """User definition."""

    # TODO: Define form fields here
    username = forms.CharField(max_length=255, required=False)
    password = forms.CharField(
        widget=forms.PasswordInput, max_length=255, required=False)
    first_name = forms.CharField(max_length=255, required=False)
    last_name = forms.CharField(max_length=255, required=False)
    email = forms.EmailField(required=False)
    img_url = forms.ImageField(required=False)


class ArticleForm(ModelForm):
    """ArticleForm definition."""

    class Meta:
        model = article
        fields = ['title', 'content', 'category', 'imgurl']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'title', 'class': 'form-control'}),
            'content': forms.Textarea(attrs={'placeholder': 'content', 'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}, choices=[('politik', 'politik'), ('agama', 'agama'), ('education', 'education')]),
            'imgurl': forms.FileInput(attrs={'class': 'form-control-file'})
        }
    # menggunakan forms.form
    # # TODO: Define form fields here
    # title = forms.CharField(widget=forms.TextInput(
    #     attrs={'placeholder': 'title', 'class': 'form-control'}), max_length=255, required=False)
    # content = forms.CharField(widget=forms.Textarea(
    #     attrs={'placeholder': 'content', 'class': 'form-control'}), required=False)
    # category = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=[
    #                              ('politik', 'politik'), ('agama', 'agama'), ('education', 'education')], required=False)
    # imgurl = forms.ImageField(required=False,)


class LoginForm(forms.Form):
    """User definition."""

    # TODO: Define form fields here
    username = forms.CharField(max_length=255, required=False)
    password = forms.CharField(
        widget=forms.PasswordInput, max_length=255, required=False)
