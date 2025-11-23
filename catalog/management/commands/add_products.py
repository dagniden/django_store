from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Add test products to the database'
    Product.objects.all().delete()
    Category.objects.all().delete()

    def handle(self, *args, **kwargs):
        category1, _ = Category.objects.get_or_create(name='Игры', description='Категория с компьютерными играми')

        games = [
            {'name': 'The Witcher 3: Wild Hunt', 'description': 'Action role-playing game', 'category': category1,
             "price": 1999},
            {'name': 'Cyberpunk 2077', 'description': 'Role-playing game', 'category': category1, "price": 2499},
            {'name': 'Red Dead Redemption 2', 'description': 'Action-adventure game', 'category': category1,
             "price": 2299},
            {'name': 'Grand Theft Auto V', 'description': 'Action-adventure game', 'category': category1,
             "price": 2999},
        ]

        for game_data in games:
            game, created = Product.objects.get_or_create(**game_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added book: {game.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Book already exists: {game.name}'))
