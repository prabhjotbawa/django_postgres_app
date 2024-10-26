import os

from django.http import HttpResponse
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
    return render(request, 'home.html', {'form': form, 'items': items,
                                         'env_value': os.environ.get('NODE_NAME', 'Default Node')})


def get_data_inserted(request):
    if request.method == 'GET':
        row_count = MyModel.objects.count()
        return HttpResponse(row_count)
