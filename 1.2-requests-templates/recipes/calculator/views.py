from django.shortcuts import render
from django.http import HttpResponse
from pprint import pprint

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


def list_dishes(request):
    dishes = DATA.keys()
    return HttpResponse(f'{dishes}')


def omlet(request):
    person = request.GET.get('servings', 1)
    context = {'recipe' : {}}
    for k, v in DATA['omlet'].items() :
        context['recipe'].update({k : v * int(person)})
        print(k, v, type(v))
    print('- 8 - ' * 10)
    pprint(context)
    print(person, type(person))
    return render(request, 'calculator/index.html', context)

def pasta(request):
    person = request.GET.get('servings', 1)
    context = {'recipe' : {}}
    for k, v in DATA['pasta'].items() :
        context['recipe'].update({k : v * int(person)})
        print(k, v, type(v))
    print('- 8 - ' * 10)
    pprint(context)
    print(person, type(person))
    return render(request, 'calculator/index.html', context)

def buter(request):
    person = request.GET.get('servings', 1)
    context = {'recipe' : {}}
    for k, v in DATA['buter'].items() :
        context['recipe'].update({k : v * int(person)})
        print(k, v, type(v))
    print('- 8 - ' * 10)
    pprint(context)
    print(person, type(person))
    return render(request, 'calculator/index.html', context)
