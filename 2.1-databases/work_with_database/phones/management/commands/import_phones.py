import csv
import re

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            list_ = re.findall(r'\S', phone['name'])
            slug = ''.join(list_)
            tel = Phone(name= phone['name'], 
                        price= phone['price'], 
                        image= phone['image'], 
                        release_date= phone['release_date'], 
                        lte_exists= phone['lte_exists'],
                        slug= slug)
            tel.save()
        print('data uploaded')