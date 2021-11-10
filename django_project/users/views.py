from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from .forms import ProfileForm
from django.contrib import messages

# Create your views here.


def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid():
            user_form.save()
            profile_form.save()
            #username = form.cleaned_data.get('Custom.username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        user_form = UserRegisterForm()
        profile_form = ProfileForm()
    return render(request, 'users/register.html', {'user_form': user_form, 'profile_form': profile_form})