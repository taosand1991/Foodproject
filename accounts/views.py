from django.shortcuts import render, redirect

from recipes.form import RegistrationForm, ProfileForm, ChangePassword, UserEdit, ProfileEdit
from recipes.models import Movie
from accounts.models import Profile
from django.contrib import messages
from django.contrib.auth import authenticate, login, update_session_auth_hash


def register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST or None)
        profile_form = ProfileForm(data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password2']
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Your account has been created')
            return redirect('home')
        else:
            messages.error(request, 'There is an error with your form')
    else:
        user_form = RegistrationForm()
        profile_form = ProfileForm()
    return render(request, 'accounts/signup.html', {'user_form': user_form, 'profile_form': profile_form})


def profile(request):
    users = Profile.objects.all()

    return render(request, 'accounts/profile.html', {'users': users})


# def change_password(request):
#     if request.method == 'POST':
#         form = ChangePassword(data=request.POST, user=request.user)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)
#             messages.success(request, 'Your account has been updated')
#             return redirect('profile')
#
#     else:
#         form = ChangePassword(user=request.user)
#     return render(request, 'accounts/password_change_form.html', {'form': form})

def user_edit(request):
    if request.method == 'POST':
        user_edited = UserEdit(request.POST, instance=request.user)
        profile_edit = ProfileEdit(request.POST or None, files=request.FILES, instance=request.user.profile)
        if user_edited.is_valid() and profile_edit.is_valid():
            user_edited.save()
            profile_edit.save()
            messages.success(request, 'Your profile has been updated')
            return redirect('profile')
    else:
        user_edited = UserEdit(instance=request.user)
        profile_edit = ProfileEdit(instance=request.user.profile)
    return render(request, 'accounts/update.html', {'user_edited': user_edited, 'profile_edit': profile_edit})
