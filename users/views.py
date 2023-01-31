from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.urls import reverse

from users.forms import LoginForm


def user_detail_view(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        return render(request, "users/detail.html", {'user': user})
    except User.DoesNotExist:
        raise Http404('找不到用户')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data.get('username'),
                                password=form.cleaned_data.get('password'))
            if user is not None:
                login(request, user)
                next_url = request.POST.get('next')
                return redirect(next_url)
            else:
                form.add_error(None, "请检查用户名和密码是否正确")

    else:
        if request.user.is_authenticated:
            return redirect(request.GET.get('next', reverse('index')))

        form = LoginForm()
    return render(request, "users/login.html", {'form': form})


def logout_view(request):
    logout(request)
    return redirect(request.GET.get('next', reverse('index')))
