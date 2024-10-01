from django.shortcuts import render, redirect
from .models import MyModel
from .forms import MyModelForm


def home(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MyModelForm()

    items = MyModel.objects.all()
    return render(request, 'home.html', {'form': form, 'items': items})