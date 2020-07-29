from django.shortcuts import render
from .forms import UserForm, UserProfileForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def homepage(request):
    cont = {}
    return render(request, 'basic/homepage.html', cont)


def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                print('Logged in')
                return HttpResponseRedirect(reverse('basic:home'))
            else:
                return HttpResponse("Your account is not active")

        else:
            return HttpResponse('Login Failed')

    else:
        return render(request, 'basic/login.html',{})


def register(request):

    registered = False

    if request.method == "POST":

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            if 'birthdate' in request.POST:
                profile = profile_form
                profile.save(commit=False)
                profile.user = user
                profile.save()

            registered = True
            print('it is OK!')
        else:
            print(user_form.errors, profile_form.errors)
            return HttpResponse('something is wrong')
    else:
        user = UserForm()
        profile = UserProfileForm()

    return render(request, 'basic/register.html', {'user': user, 'profile': profile, 'registered': registered})


@login_required
def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse('basic:home'))