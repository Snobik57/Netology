from django.shortcuts import render, redirect
from django.urls import reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def index(request):
    return render(request, 'calculator/index.html')


def omlet(request):
    context = {
        'recipe': DATA['omlet']
    }
    servings = request.GET.get('servings')
    if servings:
        context['recipe'] = {key: value * int(servings) for key, value in context['recipe'].items()}

    return render(request, 'calculator/index.html', context)


def pasta(request):
    context = {
        'recipe': DATA['pasta']
    }
    servings = request.GET.get('servings')
    if servings:
        context['recipe'] = {key: value * int(servings) for key, value in context['recipe'].items()}

    return render(request, 'calculator/index.html', context)


def buter(request):
    context = {
        'recipe': DATA['buter']
    }
    servings = request.GET.get('servings')
    if servings:
        context['recipe'] = {key: value * int(servings) for key, value in context['recipe'].items()}

    return render(request, 'calculator/index.html', context)
