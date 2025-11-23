from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Add test products to the database'

    def handle(self, *args, **kwargs):
        # Удаление существующих данных
        Product.objects.all().delete()
        Category.objects.all().delete()
        self.stdout.write(self.style.WARNING('Все продукты и категории удалены'))

        # Загрузка данных из фикстуры
        call_command('loaddata', 'catalog.json')
        self.stdout.write(self.style.SUCCESS('Данные успешно загружены из фикстуры catalog.json'))
