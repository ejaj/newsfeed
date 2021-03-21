from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django.contrib.auth.models import User
from .models import UserNewsSetting
from news.models import Sources


class SignUpForm(UserCreationForm):
    """
    User sing up form.
    """
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Please enter your user name'}),
        required=True)
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Please enter your first name'}),
        required=False, max_length=30)

    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Please enter your second name'}),
        required=False, max_length=30)

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Please enter your valid email'}), max_length=254)

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Please enter your password'}), max_length=254)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Please enter your confirm password'}), max_length=254)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class SigninForm(AuthenticationForm):
    """
    User Signin Form.
    """
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Please enter your user name'}),
        required=True)

    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Please enter your password'}), max_length=254)

    class Meta:
        model = User
        fields = ('username', 'password',)


class PasswordResetForm(PasswordResetForm):
    """
    User Password reset form.
    """
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}), max_length=254, required=True)

    class Meta:
        model = User
        fields = ('email')


class UserNewsSettingForm(forms.ModelForm):
    """
    User News Setting form.
    """
    countries = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=[(source.country, source.country) for source in Sources.objects.distinct('country')]
    )

    news_source = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=[(source.name, source.name) for source in Sources.objects.distinct('name')]
    )

    keywords = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=[(source.category, source.category) for source in Sources.objects.distinct('category')]
    )

    class Meta:
        model = UserNewsSetting
        fields = ('countries', 'news_source', 'keywords',)
