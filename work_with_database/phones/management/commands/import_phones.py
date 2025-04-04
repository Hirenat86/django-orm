import csv

from django.core.management.base import BaseCommand
from django.utils.text import slugify
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r', encoding='utf-8') as file:
            phones = csv.DictReader(file, delimiter=';')
            # next(phones)
            for phone in phones:
                new_phone = Phone(
                    id = phone['id'],
                    name = phone['name'],
                    image = phone['image'],
                    price = phone['price'],
                    release_date = phone['release_date'],
                    lte_exists = phone['lte_exists'] == 'True',
                    slug = slugify(phone['name'])
                )
                new_phone.save()
