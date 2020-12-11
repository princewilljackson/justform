from django.shortcuts import render, redirect
from .forms import UserDataForm


# Create your views here.
def home(request):
    """Renders the index page."""
    if request.method == 'POST':
        form = UserDataForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('kin:success')
    else:
        form = UserDataForm()
    return render(request, 'index.html', {
        'form': form
    })


def success(request):
    return render(request, 'success.html')