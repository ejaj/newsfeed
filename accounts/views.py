from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.mail import BadHeaderError, send_mail
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import SignUpForm, SigninForm, PasswordResetForm, UserNewsSettingForm
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.http import HttpResponse
from .models import UserNewsSetting
from django.contrib.auth.decorators import login_required


# Create your views here.

def signin(request):
    """
    Create user signin form.
    Check user logged in if logged in, redirect to index route
    If user not logged in then, getting post data, matching user name and password and if user found then log in the user and
    redirect to index
    If failed all mentioned case then redirect to singin page.
    :param request:
    :return:
    """
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, "Logged in successfully!")
            return redirect('index')
        else:
            form = SigninForm(request.POST)
            return render(request, 'accounts/signin.html', {'form': form})
    else:
        form = SigninForm()
        return render(request, 'accounts/signin.html', {'form': form})


def signup(request):
    """
    Create user signup form
    Check user logged in if logged in, redirect to index route
    If user not logged in then create new user, log in this user and redirect to index
    User information store to model:User.
    :param request:
    :return:
    """
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            messages.info(request, "Logged in successfully!")
            return redirect('index')
        else:
            return render(request, 'accounts/signup.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'accounts/signup.html', {'form': form})


@login_required(login_url='signin')
def signout(request):
    """
    Log out, logged in user.
    :param request:
    :return:
    """
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('index')


def password_reset_request(request):
    """
    Create user password reset from
    Get user by email if user exist then password reset link send to user email.
    :param request:
    :return:
    """
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))

            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "accounts/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'News Feed',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    template = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, template, 'kejaj.777@gmail.com', [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("/accounts/password_reset/done/")

    form = PasswordResetForm()
    return render(request, 'accounts/password_reset.html', {"form": form})


@login_required(login_url='signin')
def user_news_setting(request):
    """
    Get news setting information from model:UserNewsSetting by user.
    :param request:
    :return:
    """
    context = {}
    context["user_settings"] = UserNewsSetting.objects.filter(user_id=request.user.id)
    return render(request, 'accounts/news_setting.html', context)


@login_required(login_url='signin')
def add_user_news_setting(request):
    """
    Crete From for adding news setting by user
    Date store to model:UserNewsSetting.
    :param request:
    :return:
    """
    if request.method == "POST":
        form = UserNewsSettingForm(request.POST)
        if form.is_valid():
            comma = ","
            countries = form.cleaned_data['countries']
            countries_list = comma.join(countries)
            news_source = form.cleaned_data['news_source']

            news_source_list = comma.join(news_source)

            keywords = form.cleaned_data['keywords']
            keywords_list = comma.join(keywords)
            obj, created = UserNewsSetting.objects.update_or_create(
                user_id=request.user.id,
                defaults={
                    'countries': countries_list,
                    'news_source': news_source_list,
                    'keywords': keywords_list,

                },
            )
            messages.info(request, "News setting updated")
            return redirect('user_news_setting')
    form = UserNewsSettingForm()
    return render(request, 'accounts/add_news_setting.html', {"form": form})
