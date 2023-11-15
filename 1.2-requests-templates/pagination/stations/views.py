from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from pagination.settings import BUS_STATION_CSV
from django.core.paginator import Paginator
import csv

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    with open(BUS_STATION_CSV, encoding='utf-8') as f :
        reader = csv.DictReader(f)
        list_dicts = [i for i in reader]
        test = [
            {'Name': 'mama', 'Street': 'papa', 'District': 'ded'},
            {'Name': 'mama', 'Street': 'papa', 'District': 'ded'}
        ]

        page_number = request.GET.get('page', 1)
        pagi = Paginator(list_dicts, 3)
        page = pagi.get_page(page_number)

        context = {
            'bus_stations': pagi,
            'page': page,
        }
        return render(request, 'stations/index.html', context)



        # return HttpResponse(reader)