from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Загружает тестовые продукты'

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        call_command('loaddata', 'categories.json', app_label='catalog')
        call_command('loaddata', 'products.json', app_label='catalog')

        self.stdout.write(self.style.SUCCESS(f'Successfully loaded data from fixture'))
