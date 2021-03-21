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
    """

    country_list = (
        ('bd', 'Bangladesh'),
        ('ar', 'Argentina'),
        ('au', 'Australia'),
        ('br', 'Brazil'),
        ('ca', 'Canada'),
        ('de', 'Germany'),
        ('es', 'Spain'),
        ('fr', 'France'),
        ('gb', 'United Kingdom'),
        ('ie', 'Ireland'),
        ('in', 'India'),
        ('is', 'Israel'),
        ('it', 'Italy'),
        ('nl', 'Netherlands'),
        ('no', 'Norway'),
        ('pk', 'Pakistan'),
        ('ru', 'Russia'),
        ('sa', 'Saudi Arabia'),
        ('se', 'Sweden'),
        ('us', 'United States'),
        ('za', 'South Africa'),
    )

    source_list = (
        ('ABC News', 'ABC News'),
        ('ABC News (AU)', 'ABC News (AU)'),
        ('Aftenposten', 'Aftenposten'),
        ('Al Jazeera English', 'Al Jazeera English'),
        ('ANSA.it', 'ANSA.it'),
        ('Argaam', 'Argaam'),
        ('Ars Technica', 'Ars Technica'),
        ('Ary News', 'Ary News'),
        ('Associated Press', 'Associated Press'),
        ('Australian Financial Review', 'Australian Financial Review'),
        ('Axios', 'Axios'),
        ('BBC News', 'BBC News'),
        ('BBC Sport', 'BBC Sport'),
        ('Bild', 'Bild'),
        ('Blasting News (BR)', 'Blasting News (BR)'),
        ('Bloomberg', 'Bloomberg'),
        ('Business Insider', 'Business Insider'),
        ('Business Insider (UK)', 'Business Insider (UK)'),
        ('CBC News', 'CBC News'),
        ('CBS News', 'CBS News'),
        ('CNN', 'CNN'),
        ('CNN Spanish', 'CNN Spanish'),
        ('Crypto Coins News', 'Crypto Coins News'),
        ('Entertainment Weekly', 'Entertainment Weekly'),
        ('ESPN', 'ESPN'),
        ('ESPN Cric Info', 'ESPN Cric Info'),
        ('Financial Post', 'Financial Post'),
        ('Football Italia', 'Football Italia'),
        ('Fox News', 'Fox News'),
        ('Fox Sports', 'Fox Sports'),
        ('Google News', 'Google News'),
        ('Google News (Argentina)', 'Google News (Argentina)'),
        ('Google News (Australia)', 'Google News (Australia)'),
        ('Google News (Brasil)', 'Google News (Brasil)'),
        ('Google News (Canada)', 'Google News (Canada)'),
        ('Google News (France)', 'Google News (France)'),
        ('Google News (India)', 'Google News (India)'),
        ('Google News (Israel)', 'Google News (Israel)'),
        ('Google News (Italy)', 'Google News (Italy)'),
        ('Google News (Russia)', 'Google News (Russia)'),
        ('Google News (Saudi Arabia)', 'Google News (Saudi Arabia)'),
        ('Google News (UK)', 'Google News (UK)'),
        ('Hacker News', 'Hacker News'),
        ('Independent', 'Independent'),
        ('Medical News Today', 'Medical News Today'),
        ('MSNBC', 'MSNBC'),
        ('MTV News', 'MTV News'),
        ('MTV News (UK)', 'MTV News (UK)'),
        ('National Geographic', 'National Geographic'),
        ('National Review', 'National Review'),
        ('News24', 'News24'),
        ('NBC News', 'NBC News'),
        ('New Scientist', 'New Scientist'),
        ('New York Magazine', 'New York Magazine'),
        ('NFL News', 'NFL News'),
        ('NHL News', 'NHL News'),
        ('TechCrunch', 'TechCrunch'),
        ('TechCrunch (CN)', 'TechCrunch (CN)'),
        ('The Times of India', 'The Times of India'),
        ('The Verge', 'The Verge'),
        ('The Wall Street Journal', 'The Wall Street Journal'),
        ('The Washington Post', 'The Washington Post'),
        ('The Washington Times', 'The Washington Times'),
        ('Time', 'Time'),
        ('USA Today', 'USA Today'),
        ('Wired', 'Wired'),
        ('Wired.de', 'Wired.de'),
        ('Xinhua Net', 'Xinhua Net'),
        ('Ynet', 'Ynet'),
    )

    keywords = (
        ('business', 'Business'),
        ('entertainment', 'Entertainment'),
        ('general', 'General'),
        ('health', 'Health'),
        ('science', 'Science'),
        ('sports', 'Sports'),
        ('technology', 'Technology'),

    )

    countries = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=country_list
    )

    news_source = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=source_list
    )

    keywords = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=keywords
    )

    class Meta:
        model = UserNewsSetting
        fields = ('countries', 'news_source', 'keywords',)
