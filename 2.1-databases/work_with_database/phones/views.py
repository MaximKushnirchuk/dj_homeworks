from django.shortcuts import render, redirect
from django.http import HttpResponse
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones_object = Phone.objects.all()

    sort_option = request.GET.get('sort')
    if sort_option == 'name':
        phones = phones_object.order_by('slug')
    elif sort_option == 'min_price':
        phones = phones_object.order_by('price')
    elif sort_option == 'max_price':
        phones = phones_object.order_by('-price')
    else : phones = phones_object

    context = {
        'phones' : phones
        }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_object = Phone.objects.filter(slug= slug)
    phone_list = [f'{one.name}, {one.price}, {one.image}, {one.release_date}, {one.lte_exists}, {one.slug}'  for one in phone_object]
    print()
    res = phone_list[0].split(',')
    print(res)
    context = {
        'phone': {
            'name': res[0],
            'price': res[1],
            'image' : res[2],
            'release_date': res[3],
            'lte_exists': res[4],
            'slug': res[5]}
        }
    return render(request, template, context)