from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import login
from .models import Chat
from django.contrib.auth.decorators import login_required


@login_required
def main(request):
    chats = Chat.objects.all()
    return render(request, 'main.html', {'chats': chats})


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


@login_required
def chat(request, slug):
    chat = Chat.objects.get(slug=slug)
    return render(request, 'chat.html', {'chat': chat})