import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:
            phone_reader = csv.reader(csvfile, delimiter=';')
            next(phone_reader)
            for line in phone_reader:
                name = line[1]
                price = line[3]
                image = line[2]
                release_date = line[4]
                lte_exists = line[5]
                Phone(name=name, price=price, image=image, release_date=release_date,
                      lte_exists=lte_exists).save()

