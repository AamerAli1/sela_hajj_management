from django.shortcuts import render, redirect
from .forms import UserForm


# Create your views here.
def main_page(request):
    return render(request, 'main_page.html', {})


def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_user')
    else:
        form = UserForm()

    return render(request, 'create_user.html', {'form': form})
