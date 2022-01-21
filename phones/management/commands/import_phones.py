import csv

from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify

from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.reader(csvfile, delimiter=';')
            phone_list = []
            for i in list(phone_reader)[1:]:
                phone_list.append(i)

            for line in phone_list:
                new_phone = Phone(name = line[1],
                              price = line[3],
                              image = line[2],
                              release_date = line[4],
                              lte_exists = line[5],
                                  slug = slugify(line[1]))
                new_phone.save()
