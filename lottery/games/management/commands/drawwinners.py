from django.core.management.base import BaseCommand, CommandError
from games.models import Game

class Command(BaseCommand):
    help = 'Draws winners for games depending on their date'

    def handle(self, *args, **options):
        Game().draw_winners()