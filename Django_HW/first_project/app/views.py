import datetime
import os

from django.http import HttpResponse
from django.shortcuts import render, reverse, get_object_or_404


def home_view(request):
    template_name = 'app/home.html'

    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать директорию': reverse('workdir')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    return render(request, 'app/time.html', {'current_time': current_time})


def workdir_view(request):
    dir_ = os.listdir()
    return render(request, 'app/workdir.html', {'dir_': dir_})

