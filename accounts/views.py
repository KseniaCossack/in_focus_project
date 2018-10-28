from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def my_account(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'my_account.html')

# Create your views here.
