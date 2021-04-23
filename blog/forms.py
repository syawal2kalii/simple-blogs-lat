from django import forms


class UserForm(forms.Form):
    """User definition."""

    # TODO: Define form fields here
    username = forms.CharField(max_length=255, required=False)
    password = forms.CharField(
        widget=forms.PasswordInput, max_length=255, required=False)
    first_name = forms.CharField(max_length=255, required=False)
    last_name = forms.CharField(max_length=255, required=False)
    email = forms.EmailField(required=False)


class ArticleForm(forms.Form):
    """ArticleForm definition."""

    # TODO: Define form fields here
    title = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'title', 'class': 'form-control'}), max_length=255, required=False)
    content = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'content', 'class': 'form-control'}), required=False)
    category = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=[
                                 ('politik', 'politik'), ('agama', 'agama'), ('education', 'education')], required=False)
