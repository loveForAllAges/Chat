from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import login


def main(request):
    return render(request, 'main.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main')
    else:
        form = SignupForm()

        return render(request, 'signup.html', {'form': form})
